from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PatientMedicineSchedule, MedicineTag, Days
from users.models import PatientProfile
from .decorators import patient_required

@patient_required
def PatientTimeTable(request):
    if request.method == "POST":
        patient = PatientProfile.objects.first()  # Choosing the default patient profile for testing only
        medicine_name = request.POST.get("medicine_name")
        medicine_dosage = request.POST.get("medicine_dosage")
        medicine_days = request.POST.getlist("medicine_days")
        medicine_gap = request.POST.get("medicine_gap") # gap between each dose in hours
        medicine_time = request.POST.get("medicine_time") # first dose time
        medicine_start_date = request.POST.get("medicine_start_date") # start date
        medicine_end_date = request.POST.get("medicine_end_date") #end date
        medicine_notes = request.POST.get("medicine_notes")
        # tags = request.POST.getlist("tags")

        try:
            medicine_schedule = PatientMedicineSchedule.objects.create(
                patient=patient,
                medicine_name=medicine_name,
                medicine_dosage=medicine_dosage,
                medicine_gap=medicine_gap,
                medicine_time=medicine_time,
                medicine_start_date=medicine_start_date,
                medicine_end_date=medicine_end_date,
                medicine_notes=medicine_notes
            )
            #adds many-to-many relationship to medicine and days
            for day in medicine_days:
                day_instance = Days.objects.get(day=day)
                medicine_schedule.medicine_days.add(day_instance)

            # Uncomment the following lines to add tags
            # for tag in tags:
            #     tag_instance = MedicineTag.objects.get(tag=tag)
            #     medicine_schedule.tags.add(tag_instance)

            print("Medicine schedule created successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

        

        context = {"hours" : range(0,24), "days": Days.objects.all(), "medicine_schedules": PatientMedicineSchedule.objects.filter(patient=patient).order_by('medicine_time')}
        return render(request, "dashboard/medicine_timetable.html", context)

    return render(request, "dashboard/medicine_timetable.html", context={"hours" : range(0,24), "days": Days.objects.all(), "medicine_schedules": PatientMedicineSchedule.objects.filter(patient=PatientProfile.objects.first())})
