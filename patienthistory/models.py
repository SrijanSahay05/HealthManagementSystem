from django.db import models

class MedicinePatientTags(models.Model):
    tag_name = models.CharField(max_length=100, verbose_name="Tag Name")

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = "Medicine Patient Tag"
        verbose_name_plural = "Medicine Patient Tags"


class DayOfWeek(models.Model):
    name = models.CharField(max_length=10, unique=True, verbose_name="Day of the Week")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Day of the Week"
        verbose_name_plural = "Days of the Week"
        ordering = ['id']


class MedicineRoutine(models.Model):
    user = models.ForeignKey(
        'users.CustomUser', 
        on_delete=models.SET_NULL, 
        null=True,
        blank=True,
        verbose_name="User"
    )
    medicine_name = models.CharField(max_length=100, verbose_name="Medicine Name")
    dosage = models.CharField(max_length=100, verbose_name="Dosage")
    time = models.TimeField(verbose_name="Time")
    days_of_week = models.ManyToManyField(DayOfWeek, verbose_name="Days of the Week")
    dosage_frequency_per_day = models.IntegerField(default=1, verbose_name="Dosage Frequency Per Day")
    dosage_frequency_per_week = models.IntegerField(default=7, verbose_name="Dosage Frequency Per Week")
    is_lifelong = models.BooleanField(default=False, verbose_name="Is Lifelong")
    duration_in_days = models.IntegerField(null=True, blank=True, verbose_name="Duration in Days")
    special_case = models.CharField(max_length=255, null=True, blank=True, verbose_name="Special Case")
    tags = models.ManyToManyField(MedicinePatientTags, verbose_name="Tags", blank=True)

    def __str__(self):
        return self.medicine_name

    class Meta:
        verbose_name = "Medicine Routine"
        verbose_name_plural = "Medicine Routines"
        ordering = ['medicine_name']


class PatientBloodPressureRecords(models.Model):
    user = models.ForeignKey(
        'users.PatientProfile', 
        on_delete=models.SET_NULL, 
        null=True,
        blank=False,
        verbose_name="User"
    )
    systolic = models.IntegerField(verbose_name="Systolic")
    diastolic = models.IntegerField(verbose_name="Diastolic")
    pulse_rate = models.IntegerField(null=True, blank=True, verbose_name="Pulse Rate")
    record_date = models.DateField(verbose_name="Record Date")
    record_time = models.TimeField(verbose_name="Record Time")

    def __str__(self):
        return f"{self.user.user.email if self.user else 'Unknown'} - {self.record_date} - {self.record_time}"

    class Meta:
        verbose_name = "Patient Blood Pressure Record"
        verbose_name_plural = "Patient Blood Pressure Records"
        ordering = ['record_date', 'record_time']