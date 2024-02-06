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

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            response.data['status'] = 'Author created successfully.'
        return response   
class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        if response.status_code == status.HTTP_204_NO_CONTENT:
            response.data = {'message': 'Author category deleted successfully.'}
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            response.data['message'] = 'Author category updated successfully.'
        return response

class BookCategoryListCreateView(generics.ListCreateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            response.data['status'] = 'category created successfully.'
        return response
class BookCategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        if response.status_code == status.HTTP_204_NO_CONTENT:
            response.data = {'message': 'Book category deleted successfully.'}
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            response.data['message'] = 'Book category updated successfully.'
        return response
class LibrarianListCreateView(generics.ListCreateAPIView):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            response.data['status'] = 'Librarian created successfully.'
        return response
class LibrarianRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        if response.status_code == status.HTTP_204_NO_CONTENT:
            response.data = {'message': 'Librarian deleted successfully.'}
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            response.data['message'] = 'Librarian updated successfully.'
        return response
class LibraryListCreateView(generics.ListCreateAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            response.data['status'] = 'Library created successfully.'
        return response
class LibraryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        if response.status_code == status.HTTP_204_NO_CONTENT:
            response.data = {'message': 'Library deleted successfully.'}
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            response.data['message'] = 'Library updated successfully.'
        return response
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            response.data['status'] = 'Book created successfully.'
        return response

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects. all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        if response.status_code == status.HTTP_204_NO_CONTENT:
            response.data = {'message': 'Book deleted successfully.'}
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            response.data['message'] = 'Book updated successfully.'
        return response
    
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
