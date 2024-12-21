# from django import forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import models
# from .models import CustomUser

# class CustomUserRegistrationForm(UserCreationForm):
#     email = forms.EmailField()
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'name', 'password1', 'password2', 'usertype']

# class CustomUserLoginForm(AuthenticationForm):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'password']

# users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class CustomRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "name", "password1", "password2"]

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'form-control'
    }))
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': 'Name',
        'class': 'form-control'
    }))
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'form-control'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'form-control'
    }))


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control'
    }))