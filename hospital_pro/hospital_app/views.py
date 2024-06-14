from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate,login,logout


def facility_list(request):
    facilities = Facility.objects.all()
    return render(request, 'admin/facility_list.html', {'facilities': facilities})

def facility_detail(request, pk):
    facility = get_object_or_404(Facility, pk=pk)
    return render(request, 'admin/facility_detail.html', {'facility': facility})

def facility_create(request):
    if request.method == 'POST':
        form = FacilityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facility_list')
    else:
        form = FacilityForm()
    return render(request, 'admin/facility_form.html', {'form': form})

def facility_delete(request,pk):
    facility = Facility.objects.get(pk = pk)
    if request.method == 'POST':
        facility.delete()
        return redirect('facility_list')
    return render(request,'admin/facility_delete.html',{'facility':facility})


def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'admin/appointment_list.html', {'appointments': appointments})

def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'admin/appointment_detail.html', {'appointment': appointment})

def appointment_delete(request,pk):
    appointment = Appointment.objects.get(pk = pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request,'admin/appointment_delete.html',{'appointment':appointment})

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
    return render(request,'admin/register.html',{'form':form})

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
                return redirect('facility_list')
    else:
        form = LoginForm()




    return render(request, 'admin/login.html', {'form': form})
