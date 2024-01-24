from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home(request):
    context = {'page' : 'Home'}
    return render(request, 'index.html', context)


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


def login_page(request):
    context = {'page' : 'Sign'}
    return render(request, 'signin.html', context)

def logout_page(request):
    return HttpResponse("Hello from logout view")

def profile_page(request):
    return HttpResponse("Hello from profile view")

def edit_profile_page(request):
    return HttpResponse("Hello from edit profile view")

def forgot_password_page(request):
    return HttpResponse("Hello from forgot password view")

def reset_password_page(request):
    return HttpResponse("Hello from reset password view")