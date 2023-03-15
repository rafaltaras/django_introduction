# maths/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib import messages

def math(request):
   return HttpResponse("Tu będzie matma")

def add(request, a, b):
	a, b = int(a), int(b)
	wynik = a+b
	c = {"a":a, "b":b, "operacja": "+" ,"wynik":wynik, "title":"dodawanie"}
	return render(
    	    request=request,
    	    template_name="maths/operation.html",
    	    context=c
	)

def sub(request, a, b):
   a, b = int(a), int(b)
   wynik = a-b
   c = {"a":a, "b":b, "operacja": "-" ,"wynik":wynik}
   return render(
    	    request=request,
    	    template_name="maths/operation.html",
    	    context=c
	)

def mul(request, a, b):
   a, b = int(a), int(b)
   wynik = a*b
   c = {"a":a, "b":b, "operacja": "*" ,"wynik":wynik}
   return render(
    	    request=request,
    	    template_name="maths/operation.html",
    	    context=c
	)

def div(request, a, b):
   if int(b) == 0:
       wynik = "Error"
       messages.add_message(request, messages.ERROR, "Dzielenie przez zero!")
   else:
       wynik = a / int(b)
   c = {"a": a, "b": b, "operacja": "/", "wynik": wynik, "title": "dzielenie"}
   return render(
       request=request,
       template_name="maths/operation.html",
       context=c)
