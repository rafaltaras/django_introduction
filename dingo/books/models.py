from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.models import User

class Book(models.Model):
   title = models.CharField(max_length=15, unique=True)
   description = models.TextField()
   created = models.DateTimeField(auto_now_add=True)
   modified = models.DateTimeField(auto_now=True)
   book_cover_image = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True)
   author = models.ForeignKey(
      'books.Author',
      on_delete=models.CASCADE,
      null=True,
      blank=True
   )
   tags = models.ManyToManyField("books.Tag", related_name="books", null=True, blank=True)
   def __str__(self):
        return f"id:{self.id}, title={self.title}, description={self.description}"

class Author(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    author_bio = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"{self.name}, {self.surname}"
    
class Tag(models.Model):
   word = models.CharField(max_length=50, unique=True, null=True, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   def __str__(self):
      return f"{self.word}"
   
class Borrow(models.Model):
   book = models.ForeignKey(
      'books.Book',
      on_delete=models.PROTECT,
      unique=True
   )
   user = models.ForeignKey(
        User, on_delete=models.PROTECT, editable=False, related_name='books', null=True, blank=True)
   rent_date = models.DateTimeField(auto_now_add=True, editable=False)
   back_date = models.DateField(
        default=datetime.now()+timedelta(days=30))
   is_returned = models.BooleanField(default=True)
