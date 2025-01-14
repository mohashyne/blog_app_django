# project_root/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),                    # Admin site
    # Include articles app URLs
    path('articles/', include('articles.urls')),
    path('', views.home, name='home'),                  # Root URL (homepage)
    path('about/', views.about, name='about'),          # About page
]

urlpatterns += staticfiles_urlpatterns()
