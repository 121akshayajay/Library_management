from rest_framework import serializers
from .models import Author, BookCategory, Library, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

""" class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = '__all__' """
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

class BookSerializer(serializers.ModelSerializer):
    category = BookCategorySerializer()
    class Meta:
        model = Book
        exclude = ['library','copies_available','id']


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


