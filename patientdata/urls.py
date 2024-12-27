from django.urls import path
from patientdata import views as patientdata_views

urlpatterns = [
    path("timetable/", patientdata_views.PatientTimeTable, name="timetable"),
]