# project_root/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static  # Import static to serve media files
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('accounts/', include('accounts.urls')),
    # Include articles app URLs
    path('articles/', include('articles.urls')),
    path('', views.home, name='home'),                  # Root URL (homepage)
    path('about/', views.about, name='about'),          # About page
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
