from django.core.management.base import BaseCommand
from datetime import datetime, timedelta, time
from appointmentbooking.models import slot
from dashboard.models import UpcomingDates

class Command(BaseCommand):
    help = 'Generate timeslots for each date in UpcomingDates'

    def handle(self, *args, **kwargs):
        start_time = time(9, 0)  # Start time at 9:00 AM
        end_time = time(17, 0)   # End time at 5:00 PM
        time_delta = timedelta(minutes=15)

        upcoming_dates = UpcomingDates.objects.all()

        for upcoming_date in upcoming_dates:
            current_time = datetime.combine(upcoming_date.date, start_time)
            end_datetime = datetime.combine(upcoming_date.date, end_time)

            while current_time < end_datetime:
                slot.objects.get_or_create(date=upcoming_date, time=current_time.time())
                current_time += time_delta

        self.stdout.write(self.style.SUCCESS('Successfully generated timeslots for all upcoming dates'))