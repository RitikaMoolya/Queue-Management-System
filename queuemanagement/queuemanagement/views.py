from django.shortcuts import render, redirect 
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth import login, logout


def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contactus(request):
    return render(request, 'contactus.html')

def industries(request):
    return render(request, 'industries.html')

def salons(request):
    return render(request, 'salons.html')

def signup_view(request):
    if request.method == "POST": 
        form = SignUpForm(request.POST) 
        if form.is_valid(): 
            login(request, form.save())
            return redirect("Home")
    else:
        form = SignUpForm()
    return render(request, "signup.html", { "form": form })

def login_view(request): 
    if request.method == "POST": 
        form = AuthenticationForm(data=request.POST)
        if form.is_valid(): 
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("Home")
    else: 
        form = AuthenticationForm()
    return render(request, "login.html", { "form": form })

def logout_view(request):
    if request.method == "POST": 
        logout(request) 
        return redirect("Home")