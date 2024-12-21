from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.core.validators import RegexValidator


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ("patient", "Patient"),
        ("doctor", "Doctor"),
        ("admin_user", "Admin"),
    )
    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
    )
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

    def __str__(self):
        return f"{self.username}-{self.usertype}"
