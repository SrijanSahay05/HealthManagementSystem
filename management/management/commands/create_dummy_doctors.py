from django.core.management.base import BaseCommand
from django.utils import timezone
from users.models import CustomUser, DoctorProfile

class Command(BaseCommand):
    help = 'Create dummy users and their associated doctor profiles with specializations and other attributes'

    def handle(self, *args, **kwargs):
        first_names = [
            "Aarav", "Ishita", "Vivaan", "Ananya", "Arjun",
            "Diya", "Krishna", "Riya", "Kabir", "Sanya",
            "Rohan", "Meera", "Aryan", "Pooja", "Kunal"
        ]

        specializations = [
            "Cardiology", "Dermatology", "Neurology", "Pediatrics", "Orthopedics",
            "Gynecology", "Oncology", "Radiology", "Psychiatry", "Ophthalmology",
            "Gastroenterology", "Endocrinology", "Nephrology", "Urology", "Pulmonology"
        ]

        for first_name, specialization in zip(first_names, specializations):
            email = f"{first_name.lower()}@gmail.com"
            password = "test@123"
            username = f"{first_name.lower()}"
            user = CustomUser.objects.create_user(
                first_name=first_name,
                last_name="Doc",
                username= username,
                email=email,
                password=password,
                is_doctor=True,
                date_of_birth=timezone.now().date()
            )
            DoctorProfile.objects.create(
                user=user,
                specialization=specialization,
                appointment_duration=30,
                appointment_fees=500
            )
            self.stdout.write(self.style.SUCCESS(f"Created doctor: {first_name} with specialization in {specialization}"))

        self.stdout.write(self.style.SUCCESS('Successfully created dummy users and their doctor profiles'))