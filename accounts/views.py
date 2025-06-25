"""
Django views for user authentication and account management.

This module contains view functions for handling user registration, login, and logout
functionality for the blog application. All views use Django's built-in authentication
system and forms for security and consistency.
"""

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def signup(request):
    """
    Handle user registration (signup) functionality.

    This view processes both GET and POST requests:
    - GET: Display an empty registration form
    - POST: Process the submitted form data and create a new user account

    Args:
        request (HttpRequest): The HTTP request object containing user data

    Returns:
        HttpResponse: Either renders the signup form or redirects after successful registration

    Flow:
        1. If POST request: validate submitted form data
        2. If form is valid: create user account and automatically log them in
        3. Redirect to articles list page after successful registration
        4. If GET request or invalid form: display the signup form
    """
    if request.method == 'POST':
        # Process submitted registration form
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Create new user account
            user = form.save()
            # Automatically log in the newly registered user
            login(request, user)
            # Redirect to the main articles page
            return redirect('articles:article_list')
    else:
        # Display empty registration form for GET requests
        form = UserCreationForm()

    # Render the signup template with the form
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    """
    Handle user authentication (login) functionality.

    This view processes both GET and POST requests:
    - GET: Display an empty login form
    - POST: Authenticate user credentials and log them in

    Args:
        request (HttpRequest): The HTTP request object containing login credentials

    Returns:
        HttpResponse: Either renders the login form or redirects after successful authentication

    Flow:
        1. If POST request: validate submitted credentials
        2. If credentials are valid: log in the user
        3. Check for 'next' parameter to redirect to intended page or default to articles list
        4. If GET request or invalid credentials: display the login form

    Note:
        Supports redirect to originally requested page via 'next' parameter for better UX
    """
    if request.method == 'POST':
        # Process submitted login form with user credentials
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Extract authenticated user from the form
            user = form.get_user()
            # Log in the authenticated user
            login(request, user)

            # Handle redirect after successful login
            # Check if there's a 'next' parameter to redirect to originally requested page
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                # Default redirect to articles list page
                return redirect('articles:article_list')
    else:
        # Display empty login form for GET requests
        form = AuthenticationForm()

    # Render the login template with the form
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    """
    Handle user logout functionality.

    This view processes both GET and POST requests:
    - GET: Display logout confirmation page
    - POST: Actually log out the user and redirect

    Args:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse: Either renders logout confirmation or redirects after logout

    Flow:
        1. If POST request: log out the user and redirect to logout confirmation
        2. If GET request: display logout confirmation page

    Security Note:
        Logout action only occurs on POST requests to prevent CSRF attacks
        via malicious links that could log users out unintentionally
    """
    if request.method == 'POST':
        # Log out the current user
        logout(request)
        # Redirect to logout confirmation page
        return redirect('accounts:logout')

    # Display logout confirmation page for GET requests
    return render(request, 'accounts/logout.html')
