from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from datetime import date, timedelta
from .models import Days, Dates

@receiver(post_save, sender=Days)
def create_upcoming_dates(sender, instance, created, **kwargs):
    if created:
        print(f"Creating upcoming dates for {instance}")
    today = date.today()
    for day_offset in range(90):
        target_date = today + timedelta(days=day_offset)
        if target_date.strftime("%A") == instance.name:
            Dates.objects.get_or_create(day=instance, date=target_date)
            print(f"Created date {target_date} for {instance}")
