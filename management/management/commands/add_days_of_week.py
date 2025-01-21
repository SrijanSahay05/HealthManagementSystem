from django.core.management.base import BaseCommand
from patientdata.models import Days

class Command(BaseCommand):
    help = 'Add days of the week to the Days model'

    def handle(self, *args, **kwargs):
        days_of_week = [
            "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
        ]

        for day in days_of_week:
            Days.objects.get_or_create(day=day)

        self.stdout.write(self.style.SUCCESS('Successfully added days of the week'))