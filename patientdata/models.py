from django.db import models
from users.models import PatientProfile

class Days(models.Model):
    day = models.CharField(max_length=10)

    def __str__(self):
        return self.day

class MedicineTag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag

class PatientMedicineSchedule(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=50)
    medicine_dosage = models.CharField(max_length=50)
    medicine_days = models.ManyToManyField(Days, related_name='schedules')
    medicine_frequency = models.IntegerField(help_text="Number of times the medicine should be taken per day")
    medicine_time = models.TimeField()
    medicine_start_date = models.DateField(null=True, blank=True)
    medicine_end_date = models.DateField(null=True, blank=True)
    medicine_notes = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(MedicineTag, related_name='schedules')

    def __str__(self):
        return f"{self.patient.user.email} - {self.medicine_name}"