from django import forms

class PostForm(forms.Form):
    title = forms.CharField(required=False)
    content = forms.CharField(widget=forms.Textarea, required=False)

class AuthorForm(forms.Form):
    nick = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    author_bio = forms.CharField(widget=forms.Textarea, required=False)
