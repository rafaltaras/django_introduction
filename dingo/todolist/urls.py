from django.urls import path
from .views import add_task
# from django.views.generic import ListView
# from posts.models import Post

app_name="todolist"
urlpatterns = [
   path('tasks/', add_task, name="list"),
]