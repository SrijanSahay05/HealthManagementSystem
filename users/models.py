from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ("patient", "Patient"),
        ("doctor", "Doctor"),
        ("admin", "Admin"),
    )
    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
    )
    usertype = models.CharField(
        choices=USER_TYPE_CHOICES, default="patient", max_length=100
    )
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    email = models.EmailField(unique=True)
    isPatient = models.BooleanField(default=False)
    isDoctor = models.BooleanField(default=False)
    isHospital = models.BooleanField(default=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"{self.username}-{self.usertype}"
