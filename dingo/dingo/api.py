from rest_framework import routers
from posts import api_views as posts_views
from books import api_views as books_views

router = routers.DefaultRouter()
router.register('posts', posts_views.PostViewset)
router.register('authors', posts_views.AuthorViewset)
router.register('books', books_views.BookViewset)
router.register('books_author', books_views.AuthorViewset)
# router.register('books_tag', books_views.TagViewset)
# router.register('books_borrow', books_views.BorrowViewset)