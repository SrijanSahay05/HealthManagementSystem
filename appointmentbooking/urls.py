from django.urls import path
from appointmentbooking import views as appointmentbooking_view

urlpatterns = [
    path("doctor/", appointmentbooking_view.Doctorbooking, name="doctor_booking"),
    path("doctor-search/", appointmentbooking_view.DoctorSearchView.as_view(), name="doctor_search"),
    path("doctor-detail/<int:pk>", appointmentbooking_view.doctor_detail_view, name="doctor_detail"),
    path("confirm-booking", appointmentbooking_view.ConfrimBooking, name="confirm_booking"),
]