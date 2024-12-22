from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import CustomRegistrationForm, CustomLoginForm


def register(request):
    form = CustomRegistrationForm(request.POST)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Registration successful!")
        return redirect("index")  # Replace "index" with your desired redirect URL
    return render(request, "dashboard/login_signup.html", {"form": form})


def user_login(request):
    form = CustomLoginForm(data=request.POST)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, "Login successful!")
        return redirect("index")  # Replace "index" with your desired redirect URL
    return render(request, "dashboard/login_signup.html", {"form": form})

def user_logout(request):
    logout(request)
    return ("index") 