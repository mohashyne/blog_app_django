from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request, 'accounts/signup.html')  # Render the signup.html template

def login(request):
    return render(request, 'accounts/login.html')  # Render the login.html template

def logout(request):
    return render(request, 'accounts/logout.html')  # Render the logout.html template