from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm # Import the UserCreationForm

# Create your views here.
def signup(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = UserCreationForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # If the form is valid...
            form.save()  # Save the form data to the database
            # login the user
            return redirect('articles:article_list')  # Redirect to the home page
    else:
        form = UserCreationForm()  # Create a new instance of the UserCreationForm
    return render(request, 'accounts/signup.html', {'form': form})  # Render the signup.html template

# def login(request):
#     return render(request, 'accounts/login.html')  # Render the login.html template

# def logout(request):
#     return render(request, 'accounts/logout.html')  # Render the logout.html template