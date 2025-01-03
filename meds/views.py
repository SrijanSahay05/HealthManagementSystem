from django.shortcuts import render
from .models import medicine
from .models import uses

def medhome(request):
    query = request.GET.get('q')
    if query:
        medicines = medicine.objects.filter(
            models.Q(name__icontains=query) |
            models.Q(uses__name__icontains=query)
        ).distinct()
    else:
        medicines = medicine.objects.all()

    return render(request, 'meds/medhome.html', {'medicines': medicines})
