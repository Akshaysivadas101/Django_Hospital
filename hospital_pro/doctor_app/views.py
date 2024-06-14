from django.shortcuts import render, get_object_or_404, redirect
from hospital_app.models import *
from hospital_app.forms import *
from .models import *
from .forms import *


def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'doctor/doctor_appointment_list.html', {'appointments': appointments})

def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'doctor/doctor_appointment_detail.html', {'appointment': appointment})

def medical_history_list(request):
    histories = MedicalHistory.objects.all()
    return render(request, 'doctor/medical_history_list.html', {'histories': histories})

def medical_history_detail(request, pk):
    history = get_object_or_404(MedicalHistory, pk=pk)
    return render(request, 'doctor/medical_history_detail.html', {'history': history})


def create_prescription(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_appointment_list')
    else:
        form = PrescriptionForm()
    return render(request, 'doctor/e_prescription_form.html', {'form': form})

def prescription_list(request):
    prescriptions = Prescription.objects.all()
    return render(request, 'doctor/prescription_list.html', {'prescriptions': prescriptions})

def prescription_detail(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk)
    return render(request, 'doctor/prescription_detail.html', {'prescription': prescription})

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor/doctor_list.html', {'doctors': doctors})

def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'doctor/doctor_detail.html', {'doctor': doctor})

def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'doctor/doctor_form.html', {'form': form})