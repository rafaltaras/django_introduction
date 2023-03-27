from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

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
        template_name="registration/main.html"
    )

# class view
class TemplateView(TemplateView):
    def about(request):
       return HttpResponse('result')

#     def post(self, request):
#         # <view logic>
#         return HttpResponse('result')