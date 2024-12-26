from django.contrib import admin
from .models import Days, PatientMedicineSchedule

class DaysInline(admin.TabularInline):
    model = PatientMedicineSchedule.medicine_days.through
    extra = 1

class PatientMedicineScheduleAdmin(admin.ModelAdmin):
    list_display = ('patient', 'medicine_name', 'medicine_dosage', 'medicine_frequency', 'medicine_time', 'medicine_start_date', 'medicine_end_date')
    search_fields = ('patient__user__email', 'medicine_name')
    list_filter = ('medicine_days', 'medicine_start_date', 'medicine_end_date')
    # inlines = [DaysInline]

admin.site.register(Days)
admin.site.register(PatientMedicineSchedule, PatientMedicineScheduleAdmin)
