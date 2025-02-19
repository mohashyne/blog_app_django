from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = UserCreationForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # If the form is valid...
            user = form.save()  # Save the form data to the database
            # login the user
            login(request, user)  # login the user
            return redirect('articles:article_list')  # Redirect to the home page
    else:
        form = UserCreationForm()  # Create a new instance of the UserCreationForm
    return render(request, 'accounts/signup.html', {'form': form})  # Render the signup.html template

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # login the user
            user = form.get_user() # get the user from the form
            login(request, user)  # login the user
            # here we are just redirecting the user to the home page and not logging in the user
            # we need to use the login function from django.contrib.auth to log in the user
            return redirect('articles:article_list')
    else:
        form = AuthenticationForm(data=request.POST)    
    return render(request, 'accounts/login.html', {'form':form})  # Render the login.html template


def logout_view(request):
    if request.method == 'POST':
        logout(request)  # Log out the user
        return redirect('accounts:logout')  # Redirect to the articles list page
    return render(request, 'accounts/logout.html')  # Render the logout.html template

