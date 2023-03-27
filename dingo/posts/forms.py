from django import forms
from posts.models import Post, Author

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = "__all__"
        fields = ["title", "content", "author", "image", "tags"] 

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["nick", "email", "author_bio"]
