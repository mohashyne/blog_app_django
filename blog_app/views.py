from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse('Hello, World! Welcome to our blog!')
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('About Us')
    return render(request, 'about.html')