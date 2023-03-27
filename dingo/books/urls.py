from django.urls import path
from .views import authors, books_details, authors_list, author_details, add_author
from books.models import Book

app_name="books"
urlpatterns = [
    path('list/', authors, name="list"),
    path('details/<int:id>', books_details, name="details"),
    path('author_list/', authors_list,  name="authors_list"),
    path('author_details/<int:id>', author_details,  name="author_details"),
    path('author_list/', add_author, name="add_author"),
]