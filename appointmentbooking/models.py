from django.db import models
from users.models import PatientProfile, DoctorProfile
from patientdata.models import Days
from dashboard.models import UpcomingDates
# Create your models here.
 
class doctorAvailability(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    working_days = models.ManyToManyField(Days)

    def __str__(self):
        return f"slots available for {self.doctor} on {self.working_days}"

class slot(models.Model):
    date = models.ForeignKey(UpcomingDates, on_delete=models.CASCADE)
    time = models.TimeField()

    def __str__(self):
        return f"{self.time}-{self.date}"

class appointment(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(slot, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        unique_together = ('doctor', 'time_slot')
 
    def __str__(self):
        return f"{self.patient.user.username} with {self.doctor.user.username} on {self.time_slot   }"
    

    
