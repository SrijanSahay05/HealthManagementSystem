from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "password1", "password2"]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'input-box',
                'placeholder': 'First Name',
                'required': 'required'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'input-box',
                'placeholder': 'Last Name',
                'required': 'required'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input-box',
                'placeholder': 'Email',
                'required': 'required'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'input-box',
                'placeholder': 'Password',
                'required': 'required'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'input-box',
                'placeholder': 'Confirm Password',
                'required': 'required'
            }),
        }
class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'input-box',
        'placeholder': 'Email',
        'required': 'required'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input-box',
        'placeholder': 'Password',
        'required': 'required'
    }))