from django.contrib import admin
from .models import MedicinePatientTags, MedicineRoutine, DayOfWeek, PatientBloodPressureRecords

@admin.register(MedicinePatientTags)
class MedicinePatientTagsAdmin(admin.ModelAdmin):
    search_fields = ['tag_name']
    list_display = ['tag_name']

@admin.register(DayOfWeek)
class DayOfWeekAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    list_filter = ['name']

class DayOfWeekInline(admin.TabularInline):
    model = MedicineRoutine.days_of_week.through
    extra = 0

@admin.register(MedicineRoutine)
class MedicineRoutineAdmin(admin.ModelAdmin):
    search_fields = ['medicine_name', 'user__username']
    list_display = ['medicine_name', 'user', 'dosage', 'time', 'is_lifelong', 'duration_in_days']
    list_filter = ['is_lifelong', 'days_of_week', 'user']
    filter_horizontal = ['days_of_week', 'tags']
    inlines = [DayOfWeekInline]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related('days_of_week', 'tags')
        return queryset

@admin.register(PatientBloodPressureRecords)
class PatientBloodPressureRecordsAdmin(admin.ModelAdmin):
    search_fields = ['user__user__email']
    list_display = ['user', 'systolic', 'diastolic', 'pulse_rate', 'record_date', 'record_time']
    list_filter = ['record_date', 'user']
