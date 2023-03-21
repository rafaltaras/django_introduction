from django.test import TestCase, Client
from posts.models import Post, Author

class PostViewsTest(TestCase):
    def setUp(self):
        Post.objects.create(title="Post1", content="opis")
        self.client = Client()

    def test_posts_list(self):
        response = self.client.get("/posts/list/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["posts"]), 1)
        self.assertIn('<li><a href="/posts/details/1">Post1</a></li>', response.content.decode())
