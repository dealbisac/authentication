from django.shortcuts import render
from django.http import HttpResponse 


# Create your views here.

def home_page(request):
    context = {'page' : 'Home'}
    return render(request, 'index.html', context)

def signup_page(request):
    return HttpResponse("Hello from signup view")

def login_page(request):
    return HttpResponse("Hello from login view")

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

