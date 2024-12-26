from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import CustomUser
from django.core.mail import send_mail
from django.conf import settings

@login_required
def index(request):
    user = CustomUser.objects.get(id=request.user.id)
    return render(request, "dashboard/index.html", {"user": user})

def test(request):
    return render(request, "dashboard/test.html")

def kritika(request):
    return render(request, "dashboard/kritika.html")