from django.urls import path
from .views import greetings, name

urlpatterns = [
   path('', greetings),
   path('<name>', name)
]