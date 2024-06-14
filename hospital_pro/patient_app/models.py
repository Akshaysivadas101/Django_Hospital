from django.db import models
from hospital_app.models import *
from doctor_app.models import *


from django.conf import settings

class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paypal_payment_id = models.CharField(max_length=100, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.amount}"
    
class Billing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    statement = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    insurance_info = models.TextField()
    due_date = models.DateField()