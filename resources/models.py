from django.db import models

class Days(models.Model):
    name = models.CharField(max_length=10)
    abbrevaition = models.CharField(max_length=3, unique=True, blank=True, null=True)
    def __str__(self):
        return self.name

class Dates(models.Model):
    day = models.ForeignKey(Days, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.date.strftime("%d-%m-%Y") + " " + self.day.name