from django.contrib import admin
from .models import doctorAvailability, slot, appointment

# Register your models here.
admin.site.register(doctorAvailability)
admin.site.register(slot)
admin.site.register(appointment)