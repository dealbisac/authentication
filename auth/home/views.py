from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()

# Create your views here.

@login_required(login_url='/login/')
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

        # check if email exists in database
        if not User.objects.filter(email=email).exists():
            messages.error(request, "Invalid email. Use your own student email.")
            return redirect('/login/')
        
        # authenticate user
        user = authenticate(email=email, password=password)

        if user is None:
            messages.error(request, "Invalid credentials.")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/dashboard/')
        
    return render(request, 'signin.html', context)

# Logout page view
def logout_page(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url='/login/')
# Profile page view
def profile_page(request):
    context = {'page' : 'Profile'}
    return render(request, 'profile.html', context)

def edit_profile_page(request):
    return HttpResponse("Hello from edit profile view")

def forgot_password_page(request):
    context = {'page' : 'Forgot Password'}
    return render(request, 'forgot-password.html', context)

def reset_password_page(request):
    return HttpResponse("Hello from reset password view")

def change_password_page(request):
    return HttpResponse("Hello from change password view")

@login_required(login_url='/login/')
def admin_page(request):
    context = {'page' : 'Dashboard'}
    return render(request, 'admin.html', context)