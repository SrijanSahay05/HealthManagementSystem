from django.shortcuts import render
import requests
import json
from django.conf import settings

def get_hospitals(request):
    location = request.GET.get('location')
    radius = 10000  # 10 km radius
    api_key = settings.GOOGLE_MAPS_API_KEY

    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type=hospital&key={api_key}"
    response = requests.get(url)
    hospitals = response.json()

    hospitals_json = json.dumps(hospitals['results'])
    
    return render(request, 'loc/hospitals.html', {'hospitals_json': hospitals_json})