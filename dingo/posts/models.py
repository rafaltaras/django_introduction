from django.db import models

class Post(models.Model):
   title = models.CharField(max_length=15, unique=True)
   content = models.TextField()
   created = models.DateTimeField(auto_now_add=True)
   modified = models.DateTimeField(auto_now=True)
   image = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True)
   author = models.ForeignKey(
      'posts.Author',
      on_delete=models.CASCADE,
      null=True,
      blank=True
   )
   tags = models.ManyToManyField("posts.Tag", related_name="posts", null=True, blank=True)
   def __str__(self):
        return f"id:{self.id}, title={self.title}, content={self.content}"

class Author(models.Model):
    nick = models.CharField(max_length=5)
    email = models.EmailField(max_length=70,blank=True,unique=True)
    author_bio = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"{self.nick}"
    
class Tag(models.Model):
   word = models.CharField(max_length=50, unique=True, null=True, blank=True)
   created = models.DateTimeField(auto_now_add=True)
   def __str__(self):
      return f"{self.word}"