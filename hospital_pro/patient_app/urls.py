from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('patient_list',views.patient_list,name='patient_list'),
    path('patient_detail/<int:pk>/', views.patient_detail, name='patient_detail'),
    
    
    path('patient_create/', views.patient_create, name='patient_create'),
    
    path('patient_appointment_list/', views.appointment_list, name='patient_appointment_list'),
    path('patient_appointment_detail/<int:pk>/', views.appointment_detail, name='patient_appointment_detail'),
    path('appointment_create/', views.appointment_create, name='appointment_create'),
    path('patient_medical_history_list/', views.medical_history_list, name='patient_medical_history_list'),
    path('patient_medical_history_detail/<int:pk>/', views.medical_history_detail, name='patient_medical_history_detail'),
    path('medical_history_create/', views.medical_history_create, name='medical_history_create'),
    path('billing_list/', views.billing_list, name='billing_list'),
    path('billing_detail/<int:pk>/', views.billing_detail, name='billing_detail'),
    path('billing_create/', views.billing_create, name='billing_create'),
    path('patient_facility_list/', views.facility_list, name='patient_facility_list'),
    path('patient_facility_detail/<int:pk>/', views.facility_detail, name='patient_facility_detail'),
    
    
    path('patient_prescription_list/', views.prescription_list, name='patient_prescription_list'),
    path('patient_prescription_detail/<int:pk>/', views.prescription_detail, name='patient_prescription_detail'),
    
    
    path('payment/', PaymentView.as_view(), name='payment'),
    path('payment/execute/', PaymentExecuteView.as_view(), name='payment_execute'),
    path('payment/cancel/', PaymentCancelView.as_view(), name='payment_cancel'),
    path("",views.user_login, name ='user_login'),

    path("register/",views.register, name ='register'),
]