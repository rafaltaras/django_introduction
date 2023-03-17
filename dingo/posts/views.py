from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .forms import PostForm, AuthorForm
from posts.models import Post, Author

def posts_list(request):
    posts = Post.objects.all()
    return render(
        request=request,
        template_name="posts/post_list.html",
        context={"posts": posts}
    )

def posts_details(request, id):
    post = Post.objects.get(id=id)
    author = Author.objects.get(id=id)
    return render(
        request=request,
        template_name="posts/post_details.html",
        context={"post": post, "author": author}
    )

def add_post(request):
    if request.method == "POST":
        form = PostForm(data=request.POST)

        if form.is_valid():
            Post.objects.create(form)
            messages.add_message(
                request,
                messages.SUCCESS,
                "New post created!!"
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form.errors['__all__']
            )

    form = PostForm()
    results = Post.objects.all()
    return render(
        request=request,
        template_name="posts/post_add.html",
        context={
            "results": results,
            "form": form
        }
    )