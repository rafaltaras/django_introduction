# books/admin.py
from django.contrib import admin
from books.models import Book, Author, Tag, Borrow
# Register your models here.

class BookAdmin(admin.ModelAdmin):
   list_display = ["id", "title", "author", "created"]
   list_filter = ["title"]
   search_fields = ["title"]

admin.site.register(Book, BookAdmin)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
   list_display = ['id', 'name', 'surname', 'author_bio']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
   pass

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
   pass
   # list_display = ["book", "is_returned", "user"]