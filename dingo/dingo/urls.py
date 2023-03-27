# dingo/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   # path('grappelli/', include('grappelli.urls')),
   # path('jet/', include('jet.urls', 'jet')),
   path('admin/', admin.site.urls),
   path('books/', include("books.urls")),
   path('maths/', include("maths.urls")),
   path('', include("greetings.urls")),
   path('sessions/', include("sessions.urls")),
   path('posts/', include("posts.urls")),
   path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)