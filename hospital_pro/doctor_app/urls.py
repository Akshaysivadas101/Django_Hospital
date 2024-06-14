from django.urls import path,include
from . import views




urlpatterns = [
    
    path('', views.appointment_list, name='doctor_appointment_list'),
    path('doctor_appointment_detail/<int:pk>/', views.appointment_detail, name='doctor_appointment_detail'),
    path('medical_history_list/', views.medical_history_list, name='medical_history_list'),
    path('medical_history_detail/<int:pk>/', views.medical_history_detail, name='medical_history_detail'),
    path('prescription_create/',views.create_prescription, name='create_prescription'),
    path('prescription_list/', views.prescription_list, name='prescription_list'),
    path('prescription_detail/<int:pk>/', views.prescription_detail, name='prescription_detail'),
    path('doctor_list/', views.doctor_list, name='doctor_list'),
    path('doctor_detail/<int:pk>/', views.doctor_detail, name='doctor_detail'),
    path('doctor_create/', views.doctor_create, name='doctor_create'),
    
    
    
]