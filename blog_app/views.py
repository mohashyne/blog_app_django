from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('Hello, World! Welcome to our blog!')

def about(request):
    return HttpResponse('About Us')