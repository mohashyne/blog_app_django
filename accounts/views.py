from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm # Import the UserCreationForm

# Create your views here.
def signup(request):
    form = UserCreationForm()  # Create a new instance of the UserCreationForm
    return render(request, 'accounts/signup.html', {'form': form})  # Render the signup.html template

def login(request):
    return render(request, 'accounts/login.html')  # Render the login.html template

def logout(request):
    return render(request, 'accounts/logout.html')  # Render the logout.html template