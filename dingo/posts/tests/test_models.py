from django.test import TestCase, Client
from posts.models import Post, Author
from posts.forms import PostForm, AuthorForm



class PostsModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title="Post1")

    def test_post_str(self):
        p1 = Post.objects.get(title="Post1")
        self.assertEqual(str(p1), "id:1, title=Post1, content=")

class AuthorModelTest(TestCase):
    def setUp(self):
        Author.objects.create(nick="Rafal")
        Author.objects.create(email="rafal@rafal.com")

    def test_result_str(self):
        a1 = Author.objects.get(nick="Rafal")
        a2 = Author.objects.get(email="rafal@rafal.com")
        self.assertEqual(str(a1), 'id:1, nick=Rafal, email=')
        self.assertEqual(str(a2), 'id:2, nick=, email=rafal@rafal.com')