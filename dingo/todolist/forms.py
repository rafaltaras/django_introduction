from django import forms
from todolist.models import Task, Author

# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ["done", "task", "content", "author"] 
#         labels = {"done": "label for done"}


# class TaskForm(forms.Form):
#         done = forms.BooleanField(required=False)
#         task = forms.CharField(required=False)
#         content = forms.TextInput(required=False)


#         # def clean(self):
#         #     cleaned_data = super().clean()
#         #     value = cleaned_data.get('value')
#         #     error = cleaned_data.get('error')


class TaskForm(forms.Form):
    done = forms.BooleanField(required=False)
    task = forms.CharField(required=True)
    content= forms.CharField(widget=forms.Textarea)
    
    def clean(self):
        cleaned_data = super().clean()
        done = cleaned_data.get('done')
        task = cleaned_data.get('task')
        content = cleaned_data.get('content')
