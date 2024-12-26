import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=False)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    gender = models.CharField(
        max_length=6, choices=GENDER_CHOICES, blank=True, null=True
    )
    date_of_birth = models.DateField(blank=True, null=True)
    is_patient = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=False)
    is_healthcare_provider = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.is_patient and not hasattr(self, 'patient_profile'):
            PatientProfile.objects.create(user=self)


class PatientProfile(models.Model):
    BLOOD_GROUP_CHOICES = (
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-"),
    )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='patient_profile')
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    is_bp_patient = models.BooleanField(default=False)
    is_diabetic = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
