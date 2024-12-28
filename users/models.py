import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # GENDER_CHOICES = (
    #     ("male", "Male"),
    #     ("female", "Female"),
    # )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    username =  models.CharField(max_length=30, unique=False, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    # gender = models.CharField(
    #     max_length=6, choices=GENDER_CHOICES, blank=True, null=True
    # )
    date_of_birth = models.DateField(blank=True, null=True)
    is_patient = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=False)
    is_healthcare_provider = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return  self.email
    
class Hospital(models.Model):
    hospital_name = models.CharField(max_length=100)

    def __str__(self):
        return self.hospital_name



class PatientProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3, blank=True, null=True)
    bp_patient = models.BooleanField(default=False, blank=True, null=True)
    diabetes_patient = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return f"Patient Profile for: {self.user.email}"
    
class DoctorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=50, blank=True, null=True)
    appointment_duration = models.IntegerField(help_text="Duration of each appointment in minutes", blank=True, null=True)
    appointment_fees = models.IntegerField(help_text="Fees for each appointment in INR", blank=True, null=True)
    
    # hospitals = models.ManyToManyField(Hospital, related_name='doctors') #Think how to use this     


    def __str__(self):
        return f"Doctor Profile for: {self.user.email}"


    


