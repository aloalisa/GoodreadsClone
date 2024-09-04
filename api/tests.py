from django.test import TestCase
from rest_framework.authtoken.admin import User
from rest_framework.test import APITestCase

# Create your tests here.
from books.models import Book, BookReview

class BookReviewTestCase(APITestCase):

    def test_book_review_detail(self):
        book=Book.objects.create(title='Test Book', description='', isbn='12345')
        br=BookReview.objects.create(book=book, stars_given=5, comment='good book')

        response = self.client.get('api:review-detail', kwargs={'id':br.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], br.id )
        self.assertEqual(response.data['stars_given'], 5 )
        self.assertEqual(response.data['comment'], 'good book')


