from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    author_name = models.CharField(max_length=100)

class BookCategory(models.Model):
    category = models.CharField(max_length=100)

class Librarian(models.Model):
    librarian_name = models.CharField(max_length=100)

class Library(models.Model):
    title = models.CharField(max_length=100)
    librarian = models.ForeignKey('Librarian', on_delete=models.CASCADE)
    address = models.TextField()

class Book(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    published_on = models.DateField()
    copies_available = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    category = models.ForeignKey('BookCategory', on_delete=models.CASCADE)
    language = models.CharField(max_length=50)
    pages = models.PositiveIntegerField()
    library = models.ForeignKey('Library', on_delete=models.CASCADE)
