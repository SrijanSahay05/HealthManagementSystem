from django.contrib import admin
from .models import medicine
from .models import uses

admin.site.register(medicine)
admin.site.register(uses)

