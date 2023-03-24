from django.shortcuts import render
from django.http import HttpResponse

def about(request):
   return render(
        request=request,
        template_name="greetings/about.html"
    )

def contact(request):
      return render(
        request=request,
        template_name="greetings/contact.html"
    )

def welcome(request):
   return render(
        request=request,
        template_name="greetings/main.html"
    )