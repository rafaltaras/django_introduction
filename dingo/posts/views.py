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
        form_post = PostForm(data=request.POST)
        author_id = request.POST['author']
        print(form_post)
        print(author_id)
                
        if form_post.is_valid():
            post = Post.objects.create(**form_post.cleaned_data)
            form_post = author_id
            post.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Created!!"
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form_post.errors['__all__']
            )

    form_post = PostForm()
    results_post = Post.objects.all()
    author = Author.objects.all()
    return render(
        request=request,
        template_name="posts/post_add.html",
        context={
            "results_post": results_post,      
            "form_post": form_post,
            "author": author,
        }
    )

def add_author(request):
    if request.method == "POST":
        form_auth = AuthorForm(data=request.POST)
                
        if form_auth.is_valid():
            Author.objects.create(**form_auth.cleaned_data)
            messages.add_message(
                request,
                messages.SUCCESS,
                "Created!!"
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form_auth.errors['__all__']
            )

    form_auth = AuthorForm()
    results_auth = Author.objects.all()
    return render(
        request=request,
        template_name="posts/auth_add.html",
        context={
            "results_auth": results_auth,      
            "form_auth": form_auth
        }
    )