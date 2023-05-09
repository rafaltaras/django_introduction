from django import forms
from posts.models import Post, Author

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = "__all__"
        fields = ["title", "content", "author", "image", "tags"] 

class AuthorForm(forms.Form):
    nick = forms.CharField(required=True)
    email= forms.EmailField(required=False)
    author_bio = forms.CharField(required=False)
    
    def clean(self):
        cleaned_data = super().clean()
        nick = cleaned_data.get('nick')
        email = cleaned_data.get('email')
        author_bio = cleaned_data.get('author_bio')

        # if email:
        #     raise forms.ValidationError("Podaj tylko jedną z wartości")
        # elif not (value or error):
        #         raise forms.ValidationError("Nie podano żadnej wartości!")
