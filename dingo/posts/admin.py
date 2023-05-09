from django.contrib import admin
from posts.models import Post, Author, Tag
# Register your models here.


#metoda pierwsza
class PostAdmin(admin.ModelAdmin):
   list_display = ["id", "title", "created", "author"]
   list_filter = ["title"]
   search_fields = ["title", "author"]

admin.site.register(Post, PostAdmin)


#metoda druga
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
   list_display = ['id', 'nick', 'email', 'author_bio']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
   pass