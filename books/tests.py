from django.test import TestCase
from django.urls import reverse

from books.models import Book


# Create your tests here.

class BooksTestCase(TestCase):
    def test_no_books(self):
        books = Book.objects.all()
        response=self.client.get(reverse('books:bookslist'))

        self.assertContains(response, 'No books found')


    def test_books_list(self):
        Book.objects.create(title='Test Title', description='Test Description')
        response=self.client.get(reverse('books:bookslist'))
        books=Book.objects.all()
        for book in books:
            self.assertContains(response,book.title)

