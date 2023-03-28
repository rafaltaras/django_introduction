from django import forms
from books.models import Book, Author, Borrow

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        fields = ["title", "description", "author", "book_cover_image", "tags"] 

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "surname", "author_bio"]

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ["book", "is_returned"]