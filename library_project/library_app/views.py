from rest_framework import generics
from .models import Author, BookCategory, Librarian, Library, Book
from .serializers import AuthorSerializer, BookCategorySerializer, LibrarySerializer, BookSerializer,BookCountSerializer,LibrarianSerializer
from rest_framework.response import Response
from rest_framework.views import APIView, status
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookCategoryListCreateView(generics.ListCreateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer

class BookCategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer

class LibrarianListCreateView(generics.ListCreateAPIView):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer

class LibrarianRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer

class LibraryListCreateView(generics.ListCreateAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

class LibraryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects. all()
    serializer_class = BookSerializer

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
