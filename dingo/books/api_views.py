from rest_framework.viewsets import ModelViewSet

from books.models import Book, Author, Tag, Borrow
from books.serializers import BookSerializer, AuthorSerializer, TagSerializer, BorrowSerializer

class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorViewset(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class TagViewset(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class BorrowViewset(ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer