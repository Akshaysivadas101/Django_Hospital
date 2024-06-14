from django.db import models
from hospital_app.models import *



class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True)
    diagnosis = models.TextField()
    medications = models.TextField()
    allergies = models.TextField()
    treatment_history = models.TextField()
    
    
    
class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    medication = models.TextField(max_length=255)
    dosage = models.CharField(max_length=50)
    instructions = models.TextField()
    date_prescribed = models.DateTimeField()

    def __str__(self):
        return f"Prescription for {self.patient} by {self.doctor}"
    
