# dingo/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dingo.api import router

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/v1/', include(router.urls)),
   path('books/', include("books.urls")),
   path('maths/', include("maths.urls")),
   path('', include("greetings.urls")),
   path('sessions/', include("sessions.urls")),
   path('posts/', include("posts.urls")),
   path('accounts/', include('django.contrib.auth.urls')),
   path('todolist/', include("todolist.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Configure Admin Titles
admin.site.site_header = "Raf App Administration"
admin.site.index_title = "App administration"