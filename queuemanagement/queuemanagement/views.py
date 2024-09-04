from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contactus(request):
    return render(request, 'contactus.html')

def industries(request):
    return render(request, 'industries.html')


