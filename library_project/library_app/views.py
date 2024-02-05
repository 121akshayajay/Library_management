from .models import Author, BookCategory, Librarian, Library, Book
from .serializers import AuthorSerializer, BookCategorySerializer, LibrarySerializer, BookSerializer,BookCountSerializer,LibrarianSerializer
from rest_framework.views import APIView, status
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated

class ObtainTokenPairWithView(TokenObtainPairView): 
    serializer_class = CustomTokenObtainPairSerializer

class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        if User.objects.filter(username=username).exists():
            return Response({'error': 'A user with that username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        data = {
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
        }
        return Response(data, status=status.HTTP_201_CREATED)

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
class BookCategoryListCreateView(generics.ListCreateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
    permission_classes = [IsAuthenticated]
class BookCategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
    permission_classes = [IsAuthenticated]
class LibrarianListCreateView(generics.ListCreateAPIView):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer
    permission_classes = [IsAuthenticated]
class LibrarianRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer
    permission_classes = [IsAuthenticated]
class LibraryListCreateView(generics.ListCreateAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = [IsAuthenticated]
class LibraryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = [IsAuthenticated]
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects. all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
class BooksByCategoryView(APIView):
    def get(self, request, category_id):
        try:
            category = BookCategory.objects.get(id=category_id)
        except BookCategory.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

        books = Book.objects.filter(category=category)
        serializer = BookCountSerializer({
            'category': BookCategorySerializer(category).data,
            'books': BookSerializer(books, many=True).data,
            'count': books.count(),
        })

        return Response(serializer.data)
