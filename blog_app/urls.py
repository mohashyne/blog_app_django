# project_root/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),                    # Admin site
    path('articles/', include('articles.urls')),        # Include articles app URLs
    path('', views.home, name='home'),                  # Root URL (homepage)
    path('about/', views.about, name='about'),          # About page
]
