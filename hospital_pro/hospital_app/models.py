from django.db import models



    

class Doctor(models.Model):
    
    doctor_name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=100)
    
class Patient(models.Model):
    
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.first_name}{self.last_name}"
    
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    reason = models.TextField()
    
class Facility(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    departments = models.TextField()