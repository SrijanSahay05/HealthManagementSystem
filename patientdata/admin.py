from django.contrib import admin
from .models import Days, PatientMedicineSchedule, MedicineTag



admin.site.register(Days)
admin.site.register(PatientMedicineSchedule)
admin.site.register(MedicineTag)