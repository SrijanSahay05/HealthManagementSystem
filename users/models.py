import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
<<<<<<< HEAD


class CustomUser(AbstractUser):
=======
import uuid
from django.core.validators import RegexValidator


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ("patient", "Patient"),
        ("doctor", "Doctor"),
        ("admin_user", "Admin"),
    )
>>>>>>> main
    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
    )
<<<<<<< HEAD
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    gender = models.CharField(
        max_length=6, choices=GENDER_CHOICES, blank=True, null=True
    )
    date_of_birth = models.DateField(blank=True, null=True)
    is_patient = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=False)
    is_healthcare_provider = models.BooleanField(default=False)
=======
    usertype = models.CharField(
        choices=USER_TYPE_CHOICES, max_length=100
    )
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=False)
    # phone = models.CharField(
    #     max_length=10,
    #     validators=[
    #         RegexValidator(
    #             regex=r"^\d{10}$",
    #             message="Phone number must be 10 digits",
    #             code="invalid_phone_number",
    #         )
    #     ],
    #     unique=True,
    # )
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    isPatient = models.BooleanField(default=False)
    isDoctor = models.BooleanField(default=False)
    isHospital = models.BooleanField(default=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
>>>>>>> main

    def __str__(self):
        return self.first_name + " " + self.last_name
