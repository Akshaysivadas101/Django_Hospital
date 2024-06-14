from django import forms
from .models import *
from hospital_app.models import *
from hospital_app.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'date_of_birth', 'contact_number', 'address','gender']
        
class PaymentForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    
class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['patient', 'statement', 'amount', 'paid', 'insurance_info', 'due_date']


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['password'].label = 'Password'
