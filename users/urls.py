from django.urls import path
from . import views as users_views
urlpatterns = [
    path("login/", users_views.login_register, name="login"),
    path("register/", users_views.login_register, name="register"),
]
