from django.shortcuts import render
import requests
import json
from .utils import get_hospitals
from urllib.parse import unquote
from django.http import Http404
from django.urls import reverse


fake_doctors = [
    {'name': 'Dr. John Doe', 'timing': '9 AM - 12 PM'},
    {'name': 'Dr. Jane Smith', 'timing': '1 PM - 4 PM'},
    {'name': 'Dr. Alice Brown', 'timing': '10 AM - 2 PM'},
    {'name': 'Dr. Bob White', 'timing': '3 PM - 6 PM'}
]



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

    # Use the same fake doctor data for all hospitals
    doctors = fake_doctors

    context = {
        'hospital': hospital,
        'doctors': doctors
    }
    return render(request, 'loc/hospital_info.html', context)
