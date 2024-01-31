from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from library_app.models import Author, BookCategory, Library, Book, Librarian
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    help = 'Bulk create authors, book categories, libraries, and books'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting bulk data creation...'))

        
        authors = [Author.objects.create(author_name=f'Author{i}') for i in range(1, 6)]

        
        librarians = [Librarian.objects.create(librarian_name=f'Librarian{i}') for i in range(1, 6)]

        
        categories = [BookCategory.objects.create(category=f'Category{i}') for i in range(1, 6)]

       
        libraries = [Library.objects.create(
            title=f'Library{i}',
            librarian=random.choice(librarians),
            address=get_random_string(length=50)
        ) for i in range(1, 6)]

       
        books = []
        for i in range(1, 101):  
            book = Book.objects.create(
                author=random.choice(authors),
                title=f'Book{i}',
                published_on=datetime.now() - timedelta(days=random.randint(1, 3650)),
                copies_available=random.randint(1, 10),
                price=random.randint(10, 100),
                category=random.choice(categories),
                language='English',
                pages=random.randint(50, 500),
                library=random.choice(libraries)
            )
            books.append(book)

        self.stdout.write(self.style.SUCCESS('Bulk data creation completed!'))
