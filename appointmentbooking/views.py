from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from users.models import DoctorProfile, CustomUser
from appointmentbooking.models import appointment, slot
# Create your views here.


def Doctorbooking(request):
    return render(request, "dashboard/booking_doctor.html")

class DoctorSearchView(ListView):
    model = DoctorProfile
    template_name = 'dashboard/doctor_search.html'
    context_object_name = 'doctors'
    paginate_by = 100

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return DoctorProfile.objects.filter(
                Q(user__first_name__icontains=query) | Q(specialization__icontains=query)
            )
        return DoctorProfile.objects.all()


def doctor_detail_view(request, pk):
    doctor = get_object_or_404(DoctorProfile, pk=pk)
    timeslots = slot.objects.all()

    if request.method == "POST":
        timeslot_id = request.POST.get('timeslot')
        timeslot = get_object_or_404(slot, id=timeslot_id)
        patient = get_object_or_404(CustomUser, id=request.user.id).patientprofile

        # Check if the doctor is already booked for the selected timeslot
        existing_appointment = appointment.objects.filter(doctor=doctor, time_slot=timeslot).exists()
        if existing_appointment:
            messages.error(request, "The doctor is already booked for this timeslot. Please choose another timeslot.")
        else:
            # Create the appointment
            new_appointment = appointment.objects.create(
                patient=patient,
                doctor=doctor,
                time_slot=timeslot
            )
            messages.success(request, "Your appointment has been successfully booked.")
            return redirect('confirm_booking')

    context = {
        'doctor': doctor,
        'timeslots': timeslots
    }
    return render(request, 'dashboard/doctor_detail.html', context)

def ConfrimBooking(request):
    return render(request, "dashboard/confirm_booking.html")