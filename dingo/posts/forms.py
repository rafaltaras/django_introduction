from django import forms
from posts.models import Post, Author

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["nick", "email", "author_bio"]
