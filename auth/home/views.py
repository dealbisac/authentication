from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {'page' : 'Home'}
    return render(request, 'index.html', context)

def signup(request):
    return HttpResponse("Hello from signup view")