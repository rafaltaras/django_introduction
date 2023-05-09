from django.db import models

class Task(models.Model):
   task = models.CharField(max_length=20, unique=True)
   content = models.TextField()
   created = models.DateTimeField(auto_now_add=True)
   modified = models.DateTimeField(auto_now=True)
   done = models.BooleanField(default=False)
   author = models.ForeignKey(
      'todolist.Author',
      on_delete=models.CASCADE,
      null=True,
      blank=True
   )
   def __str__(self):
        return f"id:{self.id}, task={self.task}, content={self.content}"
   

class Author(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return f"{self.name}"