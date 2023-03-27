from django import forms
from books.models import Book, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        fields = ["title", "description", "author", "book_cover_image", "tags"] 

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "surname", "author_bio"]
