import json
from .utils import get_hospitals
from urllib.parse import unquote
from django.http import Http404
from django.shortcuts import render
from users.models import DoctorProfile

def map(request):
    hospitals = get_hospitals()
    hospitals_json = json.dumps(hospitals)
    hospital_info_base_url = '/hospital/'

    return render(request, 'loc/map.html', {
        'hospitals_json': hospitals_json,
        'hospital_info_base_url': hospital_info_base_url
    })


def hospital_list(request):
    hospitals = get_hospitals()

    return render(request, 'loc/hospital_list.html', {'hospitals': hospitals})


def hospital_info(request, hospital_name):
    hospitals = get_hospitals()
    hospital_name = unquote(hospital_name)  # Decode the URL-encoded hospital name

    # Find the hospital by name
    hospital = next((h for h in hospitals if h['name'] == hospital_name), None)
    if not hospital:
        raise Http404("Hospital not found")

    # Query actual doctors from the DoctorProfile model
    doctors = DoctorProfile.objects.all()

    # Add timing information to each doctor
    doctor_data = []
    for doctor in doctors:
        doctor_data.append({
            'id': doctor.id,
            'name': f"Dr. {doctor.user.first_name} {doctor.user.last_name}",
            'timing': '9 AM - 6 PM'
        })

    context = {
        'hospital': hospital,
        'doctors': doctor_data
    }
    return render(request, 'loc/hospital_info.html', context)