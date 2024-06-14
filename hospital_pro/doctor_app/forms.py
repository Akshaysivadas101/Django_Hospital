from django import forms
from .models import *
from hospital_app.models import *
from hospital_app.forms import *



class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['patient','doctor','medication', 'dosage', 'instructions','date_prescribed']
        
class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields = ['patient', 'doctor','diagnosis', 'medications', 'allergies', 'treatment_history']


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['doctor_name','specialty']