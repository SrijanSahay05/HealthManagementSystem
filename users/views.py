from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser

def login_register(request):
    return render(request, "users/login_register.html")