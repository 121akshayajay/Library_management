from django.urls import path
from .views import (
    AuthorListCreateView, AuthorRetrieveUpdateDestroyView,
    BookCategoryListCreateView, BookCategoryRetrieveUpdateDestroyView,
    LibrarianListCreateView, LibrarianRetrieveUpdateDestroyView,
    LibraryListCreateView, LibraryRetrieveUpdateDestroyView,
    BookListCreateView, BookRetrieveUpdateDestroyView,BooksByCategoryView,UserRegistrationView,
    ObtainTokenPairWithView,
)   

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroyView.as_view(), name='author-detail'),

    path('categories/', BookCategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', BookCategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),

    path('librarians/', LibrarianListCreateView.as_view(), name='librarian-list-create'),
    path('librarians/<int:pk>/', LibrarianRetrieveUpdateDestroyView.as_view(), name='librarian-detail'),

    path('libraries/', LibraryListCreateView.as_view(), name='library-list-create'),
    path('libraries/<int:pk>/', LibraryRetrieveUpdateDestroyView.as_view(), name='library-detail'),

    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),

    path('categories/<int:category_id>/books/', BooksByCategoryView.as_view(), name='books-by-category'),

    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('token/', ObtainTokenPairWithView.as_view(), name='token-obtain-pair'),

]

""" http://127.0.0.1:8000/api/categories/1/books/ """