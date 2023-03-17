from django.urls import path
from .views import posts_list, posts_details, add_post

app_name="posts"
urlpatterns = [
   path('list/', posts_list, name="list"),
   path('details/<int:id>', posts_details, name="details"),
   path('post_add/', add_post, name="post_add"),
]