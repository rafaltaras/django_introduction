from django.db import models

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