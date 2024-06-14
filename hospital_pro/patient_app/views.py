from django.shortcuts import render, get_object_or_404, redirect
from hospital_app.models import *
from hospital_app.forms import *
from doctor_app.models import *
from doctor_app.forms import *
from .forms import *
from .models import *
from django.urls import reverse
from django.views import View
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import paypalrestsdk
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout



def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'patient/patient_form.html', {'form': form})


def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'patient/patient_detail.html', {'patient': patient})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient/patient_list.html', {'patients': patients})


def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'patient/appointment_list.html', {'appointments': appointments})

def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'patient/appointment_detail.html', {'appointment': appointment})

def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'patient/appointment_form.html', {'form': form})

def medical_history_list(request):
    histories = MedicalHistory.objects.all()
    return render(request, 'patient/medical_history_list.html', {'histories': histories})

def medical_history_detail(request, pk):
    history = get_object_or_404(MedicalHistory, pk=pk)
    return render(request, 'patient/medical_history_detail.html', {'history': history})

def medical_history_create(request):
    if request.method == 'POST':
        form = MedicalHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_medical_history_list')
    else:
        form = MedicalHistoryForm()
    return render(request, 'patient/medical_history_form.html', {'form': form})

def billing_list(request):
    billings = Billing.objects.all()
    return render(request, 'patient/billing_list.html', {'billings': billings})

def billing_detail(request, pk):
    billing = get_object_or_404(Billing, pk=pk)
    return render(request, 'patient/billing_detail.html', {'billing': billing})

def billing_create(request):
    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('billing_list')
    else:
        form = BillingForm()
    return render(request, 'patient/billing_form.html', {'form': form})

def facility_list(request):
    facilities = Facility.objects.all()
    return render(request, 'patient/facility_list.html', {'facilities': facilities})

def facility_detail(request, pk):
    facility = get_object_or_404(Facility, pk=pk)
    return render(request, 'patient/facility_detail.html', {'facility': facility})

def prescription_list(request):
    prescriptions = Prescription.objects.all()
    return render(request, 'patient/prescription_list.html', {'prescriptions': prescriptions})

def prescription_detail(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk)
    return render(request, 'patient/prescription_detail.html', {'prescription': prescription})
    

paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE,  # "sandbox" or "live"
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET,
})

@method_decorator(login_required, name='dispatch')
class PaymentView(View):
    template_name = 'patient/payment_form.html'

    def get(self, request):
        form = PaymentForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PaymentForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            payment = paypalrestsdk.Payment({
                "intent": "sale",
                "payer": {
                    "payment_method": "paypal"
                },
                "redirect_urls": {
                    "return_url": request.build_absolute_uri(reverse('payment_execute')),
                    "cancel_url": request.build_absolute_uri(reverse('payment_cancel'))
                },
                "transactions": [{
                    "item_list": {
                        "items": [{
                            "name": "Order",
                            "sku": "item",
                            "price": str(amount),
                            "currency": "USD",
                            "quantity": 1
                        }]
                    },
                    "amount": {
                        "total": str(amount),
                        "currency": "USD"
                    },
                    "description": "Payment for order"
                }]
            })

            if payment.create():
                Payment.objects.create(
                    user=request.user,
                    amount=amount,
                    paypal_payment_id=payment.id
                )
                for link in payment.links:
                    if link.rel == "approval_url":
                        return redirect(link.href)
            else:
                print(payment.error)
                return HttpResponse("An error occurred during the payment creation process.")
        return render(request, self.template_name, {'form': form})
    
@method_decorator(login_required, name='dispatch')
class PaymentExecuteView(View):
    def get(self, request):
        payment_id = request.GET.get('paymentId')
        payer_id = request.GET.get('PayerID')

        payment = paypalrestsdk.Payment.find(payment_id)
        if payment.execute({"payer_id": payer_id}):
            payment_instance = get_object_or_404(Payment, paypal_payment_id=payment_id)
            payment_instance.status = 'completed'
            payment_instance.save()
            return HttpResponse("Payment executed successfully.")
        else:
            return HttpResponse("Payment execution failed.")


@method_decorator(login_required, name='dispatch')
class PaymentCancelView(View):
    def get(self, request):
        return HttpResponse("Payment cancelled.")
    
    
def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            raw_password= form.cleaned_data.get('password1')
            user=authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request,'patient/register.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('patient_list')
    else:
        form = LoginForm()




    return render(request, 'patient/login.html', {'form': form})