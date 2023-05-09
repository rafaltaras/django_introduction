from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from todolist.models import Task, Author

def tasks(request):
    return render(
        request=request,
        template_name="todolist/tasks.html",
    )

def add_task(request):
    # if request.method == "POST":
    #     form_post = PostForm(data=request.POST, files=request.FILES)
    #     author_id = request.POST['author']               
    #     if form_post.is_valid():
    #         data = (form_post.cleaned_data)
    #         # data["author_id"] = author_id
    #         post = Post.objects.create(**data)
    #         messages.add_message(
    #             request,
    #             messages.SUCCESS,
    #             "Created!!"
    #         )
    #     else:
    #         messages.add_message(
    #             request,
    #             messages.ERROR,
    #             form_post.errors['__all__']
    #         )

    form = TaskForm()
    tasks = Task.objects.all()
    author = Author.objects.all()
    return render(
        request=request,
        template_name="todolist/tasks.html",
        context = {
            "form": form,
            "tasks": tasks,
            "author": author,
        }
    )