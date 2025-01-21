from django.urls import path
from dashboard import views as dashboard_views

urlpatterns = [
    path("", dashboard_views.index, name="index"),  
    path("my_account/", dashboard_views.Profile, name="my_account"),
]
