from rest_framework import serializers

from books.models import Book, Author, Tag, Borrow

class BookSerializer(serializers.ModelSerializer):
   class Meta:
       model = Book
       fields = ('id', 'title', 'description', 'created', 'modified', 'book_cover_image', 'author', 'tags')

class AuthorSerializer(serializers.ModelSerializer):
   class Meta:
       model = Author
       fields = ('id', 'name', 'surname','author_bio')

class TagSerializer(serializers.ModelSerializer):
   class Meta:
       model = Tag
       fields = ('id', 'word', 'created')

class BorrowSerializer(serializers.ModelSerializer):
   class Meta:
       model = Borrow
       fields = ('id', 'book', 'user', 'rent_date', 'back_date', 'is_returned' )

