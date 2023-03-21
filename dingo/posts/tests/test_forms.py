from django.test import TestCase, Client
from posts.models import Post, Author
from posts.forms import PostForm, AuthorForm

class PostFormTest(TestCase):
    def test_post_save_correct_data(self):
        data = {"title": "To jest post", "content": "test"}
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())
        r = form.save()
        self.assertIsInstance(r, Post)
        self.assertEqual(r.title, "To jest post")

class AuthorFormTest(TestCase):
    def test_author_save_correct_data(self):
        data = {"nick": "nick1", "email": "email@email.com"}
        self.assertEqual(len(Author.objects.all()), 0)
        form = AuthorForm(data=data)
        self.assertTrue(form.is_valid())
        r = form.save()
        self.assertIsInstance(r, Author)
        self.assertEqual(r.nick, "nick1")
