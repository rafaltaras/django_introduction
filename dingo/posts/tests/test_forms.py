from django.test import TestCase, Client
from posts.models import Post, Author
from posts.forms import PostForm, AuthorForm

class PostFormTest(TestCase):
    def test_post_save_correct_data(self):
        data = {"title": "To jest post"}
        form = PostForm(data=data)
        print(form)
        self.assertTrue(form.is_valid())
        # r = form.save()
        # self.assertIsInstance(r, Post)
        # self.assertEqual(r.value, 200)
        # self.assertIsNotNone(r.id)
        # self.assertIsNone(r.error)

# class AuthorFormTest(TestCase):
#     def test_author_save_correct_data(self):
#         data = {"value": 200}
#         self.assertEqual(len(Author.objects.all()), 0)
#         form = AuthorForm(data=data)
#         self.assertTrue(form.is_valid())
#         r = form.save()
#         self.assertIsInstance(r, Author)
#         self.assertEqual(r.value, 200)
#         # self.assertIsNotNone(r.id)
#         # self.assertIsNone(r.error)