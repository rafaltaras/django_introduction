from django.contrib import admin
from todolist.models import Task, Author


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
   list_display = ['id', 'task', 'created']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
   list_display = ['id', 'name']
