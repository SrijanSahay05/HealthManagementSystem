from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from patientdata.models import Days
from dashboard.models import UpcomingDates

class Command(BaseCommand):
    help = 'Generate upcoming dates for the next 90 days'

    def handle(self, *args, **kwargs):
        today = timezone.now().date()
        end_date = today + timedelta(days=90)
        days = Days.objects.all()

        for single_date in (today + timedelta(n) for n in range(91)):
            day_name = single_date.strftime('%A')
            matching_days = days.filter(day=day_name)
            for day in matching_days:
                UpcomingDates.objects.get_or_create(day=day, date=single_date)

        self.stdout.write(self.style.SUCCESS('Successfully generated upcoming dates for the next 90 days'))