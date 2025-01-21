from django.db import models
from patientdata.models import Days
# Create your models here.

class UpcomingDates(models.Model):
    day = models.ForeignKey(Days, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.day} - {self.date}"
    
    