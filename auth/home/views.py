from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# Home page view
def home(request):
    context = {'page' : 'Home'}
    return render(request, 'index.html', context)


# Sign up page view
def signup_page(request):
    context = {'page' : 'Sign Up'}

    # data from form
    if request.method == 'POST':
        email = request.POST.get('email')
        anonymousname = request.POST.get('anonymousname')
        password = request.POST.get('password')

        # check if email or username already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('/signup/')
        if User.objects.filter(username=anonymousname).exists():
            messages.error(request, "Username already exists.")
            return redirect('/signup/')

        # save data to database
        user = User.objects.create(
            email=email, 
            username=anonymousname
        )
        user.set_password(password)
        user.save()

        messages.success(request, "Account created successfully.")
        
        # redirect to sign in page.
        return redirect('/signup/')

    return render(request, 'signup.html', context)


# Sign in (Login) page view
def login_page(request):
    context = {'page' : 'Sign'}

    # data from form
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # check if email or username already exists
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            if user.check_password(password):
                messages.success(request, "Login successful.")
                return redirect('/profile/')
            else:
                messages.error(request, "Invalid password.")
                return redirect('/login/')
        else:
            messages.error(request, "Email does not exist.")
            return redirect('/login/')
    return render(request, 'signin.html', context)

# Logout page view
def logout_page(request):
    #logout(request)
    return redirect('/login/')

def profile_page(request):
    return HttpResponse("Hello from profile view")

def edit_profile_page(request):
    return HttpResponse("Hello from edit profile view")

def forgot_password_page(request):
    return HttpResponse("Hello from forgot password view")

def reset_password_page(request):
    return HttpResponse("Hello from reset password view")