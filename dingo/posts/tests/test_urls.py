from unittest import TestCase
from django.urls import resolve
from django.urls.exceptions import Resolver404
from posts.views import posts_list, posts_details

class TestUrls(TestCase):
   def test_resolution_for_posts_list(self):
       resolver = resolve('/posts/list/')
       self.assertEqual(resolver.func, posts_list)

   def test_resolution_for_post_details(self):
       resolver = resolve('/posts/details/1')
       self.assertEqual(resolver.func, posts_details)

   def test_arguments_should_be_integers_or_404(self):
       with self.assertRaises(Resolver404):
           resolve('/posts/listt/')