from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import CustomUser
from users.scripts import CreateDummyUsers
@login_required
def index(request):
    user = CustomUser.objects.get(id=request.user.id)

    return render(request, "dashboard/index.html", {"user": user})

def Profile(request):
    return render(request, "dashboard/my_account.html")


