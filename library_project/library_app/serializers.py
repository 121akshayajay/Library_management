from rest_framework import serializers
from .models import Author, BookCategory, Library, Book, Librarian
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        return token


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        refresh = RefreshToken.for_user(user)
        validated_data['access_token'] = str(refresh.access_token)
        validated_data['refresh_token'] = str(refresh)

        return validated_data

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = '__all__'

    def create(self, validated_data):
        category_name = validated_data['category']

        existing_category = BookCategory.objects.filter(category=category_name).first()

        if existing_category:
            raise serializers.ValidationError({'category': 'Category with this name already exists.'})

        return super().create(validated_data)

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'

class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Librarian
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Book
        fields = '__all__'


class BookCountSerializer(serializers.Serializer):
    category = BookCategorySerializer()
    books = serializers.SerializerMethodField()
    count = serializers.IntegerField()

    def get_books(self, instance):
        if 'books' in instance and isinstance(instance['books'], list):
            return instance['books']
        return [self.serialize_book(book) for book in instance['books']]

    def serialize_book(self, book):
        return BookSerializer(book, exclude=['library','copies_available','id']).data


