from rest_framework import serializers
from django.contrib.auth.models import User
from books.models import Book, BookReview


# class BookSerializer(serializers.Serializer):
#      title = serializers.CharField(max_length=200)
#      description = serializers.CharField()
#      isbn = serializers.CharField(max_length=17)

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'isbn')


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    username = serializers.CharField(max_length=200)
    email = serializers.EmailField()


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email')


# class BookReviewSerializer(serializers.Serializer):
#     stars_given=serializers.IntegerField(min_value=1, max_value=5)
#     comment=serializers.CharField()
#     book=BookSerializer()
#     user=UserSerializer()


class BookReviewSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    book=BookSerializer(read_only=True)
    user_id=serializers.IntegerField(write_only=True)
    book_id=serializers.IntegerField(write_only=True)

    class Meta:
        model = BookReview
        fields = ('id', 'stars_given', 'comment', 'book', 'user', 'book_id', 'user_id')
