from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib.auth.hashers import make_password

def login_register(request):
    
    if request.method == "POST":
        if "login_submit" in request.POST:
            login_email = request.POST.get("login_email")
            login_password = request.POST.get("login_password")
            user = authenticate(request, email=login_email, password=login_password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                return render(request, "dashboard/login_register.html", {"login_form": CustomLoginForm(), "error": "Invalid credentials."})
        elif "register_submit" in request.POST:
            register_email = request.POST.get("register_email")
            register_password = request.POST.get("register_password")
            register_confirm_password = request.POST.get("register_confirm_password")
            # print(register_email, register_password, register_confirm_password) 
            if register_password != register_confirm_password:
                return render(request, "dashboard/login_register.html", {"register_form": CustomUserCreationForm(), "error": "Passwords do not match."})
            try:
                hashed_password = make_password(register_password)
                CustomUser.objects.create(email=register_email, password=hashed_password)
                print("User created")
                user = authenticate(request, email=register_email, password=register_password)
                if user is not None:
                    login(request, user)
                else:
                    return render(request, "dashboard/login_register.html", {"login_form": CustomUserCreationForm(), "error": "Invalid credentials."})
                return redirect("index")
            except Exception as e:
                print(e)
                return render(request, "dashboard/login_register.html", {"register_form": CustomUserCreationForm(), "error": str(e)})

    return render(request, "dashboard/login_register.html")

def logout_view(request):
    logout(request)
    return redirect("index")