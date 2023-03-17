# dingo/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path('maths/', include("maths.urls")),
   path('greetings/', include("greetings.urls")),
   path('sessions/', include("sessions.urls")),
   path('posts/', include("posts.urls")),
]