from django.http import HttpResponseForbidden
from functools import wraps
from .models import PatientProfile

def patient_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if hasattr(request.user, 'patientprofile'):
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You do not have permission to access this page.")
    return _wrapped_view