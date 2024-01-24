from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

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
        address = request.POST.get('address')
        avatar = request.FILES.get('avatar')

        # save data to database
        user = User.objects.create_user(email=email, username=username, password=password)
        user.save()

        # return to home page
        return HttpResponse("Hello from signup view")
    return render(request, 'register.html', context)

def login_page(request):
    context = {'page' : 'Sign'}
    return render(request, 'login.html', context)

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