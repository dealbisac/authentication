"""
URL configuration for auth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
#from accounts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # accounts app urls
    #path('signup/', signup_page, name='signup'),
    #path('login/', login_page, name='login'),
    #path('logout/', logout_page, name='logout'),
    #path('profile/', profile_page, name='profile'),
    #path('edit-profile/', edit_profile_page, name='edit-profile'),
    #path('forgot-password/', forgot_password_page, name='forgot-password'),
    #path('reset-password/', reset_password_page, name='reset-password'),


    # home app urls
    path('', home, name='home'),
    path('signup/', signup_page, name='signup'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('profile/', profile_page, name='profile'),
    path('edit-profile/', edit_profile_page, name='edit-profile'),
    path('forgot-password/', forgot_password_page, name='forgot-password'),
    path('reset-password/', reset_password_page, name='reset-password'),
]
