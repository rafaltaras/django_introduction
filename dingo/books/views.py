from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .forms import BookForm, AuthorForm
from books.models import Book, Author, Borrow
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def books_details(request, id):
    book = Book.objects.get(id=id)
    author = Author.objects.get(id=id)
    borrow = Borrow.objects.get(id=id)
    return render(
        request=request,
        template_name="books/book_details.html",
        context={"book": book, "author": author, "borrow":borrow}
    )

def authors_list(request):
    authors = Author.objects.all()
    return render(
        request=request,
        template_name="books/author_list.html",
        context={"authors": authors}
    )

def author_details(request, id):
    author = Author.objects.get(id=id)
    books = Book.objects.all()
    return render(
        request=request,
        template_name="books/author_details.html",
        context={"author": author, "books": books}
    )

@login_required
def authors(request):
    if request.method == "POST":
        form_book = BookForm(data=request.POST, files=request.FILES)
        # author_id = request.POST['author']               
        if form_book.is_valid():
            data = (form_book.cleaned_data)
            Book.objects.create(**data)
            messages.add_message(
                request,
                messages.SUCCESS,
                "Book added!!"
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form_book.errors['__all__']
            )
    form_book = BookForm()
    form_auth = AuthorForm()
    books = Book.objects.all()
    author = Author.objects.all()
    paginator = Paginator(books, 3)
    page_number = request.GET.get('page')
    books = paginator.get_page(page_number)
    return render(
        request=request,
        template_name="books/book_list.html",
        context={  
            "form_book": form_book,
            "form_auth": form_auth,
            "books": books,
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
                "Author added!!"
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form_auth.errors['__all__']
            )

    form_auth = AuthorForm()
    authors = Author.objects.all()
    return render(
        request=request,
        template_name="books/author_list.html",
        context={
            "authors": authors,      
            "form_auth": form_auth
        }
    )
