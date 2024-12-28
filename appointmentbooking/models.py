from django.db import models
from users.models import PatientProfile, DoctorProfile, Hospital
from patientdata.models import Days




class DoctorHospitalSlots(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    hospital_name = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    visiting_days = models.ManyToManyField('Days', related_name='doctor_slots')
    visiting_time = models.TimeField()

    def __str__(self):
        return f"{self.doctor.user.get_full_name()} at {self.hospital_name.hospital_name} at {self.visiting_time}"

class Appointments(models.Model):

    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    hospital_name = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appintment_time = models.TimeField()

    def __str__(self):
        return f"Appointment for {self.patient.user.get_full_name()} with {self.doctor.user.get_full_name()} at {self.hospital_name.hospital_name}"
    