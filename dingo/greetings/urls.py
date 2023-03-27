from django.urls import path
from greetings.views import about, contact, welcome

urlpatterns = [
   path('', welcome, name="welcome"),
   path('about/', about, name="about"),
   path('contact/', contact, name="contact"),

   # path('about/', TemplateView.as_view(template_name="greetings/about.html")),

   ]