# articles/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),  # Homepage for articles
    path('about/', views.about, name='about'),          # About page for articles
    path('<slug:slug>/', views.article_detail, name='article_detail'),  # Article detail page
]
