from django.urls import path,include
from . import views




urlpatterns = [
    path('facility_list', views.facility_list, name='facility_list'),
    path('facility_detail/<int:pk>/', views.facility_detail, name='facility_detail'),
    path('facility_create/', views.facility_create, name='facility_create'),
    path('appointment_list/', views.appointment_list, name='appointment_list'),
    path('appointment_detail/<int:pk>/', views.appointment_detail, name='appointment_detail'),
    path('appointment_delete/<int:pk>/',views.appointment_delete,name = 'appointment_delete'),
    path('facility_delete/<int:pk>/',views.facility_delete,name = 'facility_delete'),
    path('',views.user_login,name='user_login'),
    path('register/',views.register, name ='register'),
    path("doctor/",include('doctor_app.urls')),
    path('patient/',include('patient_app.urls')),
    path('logout/',views.logout,name='logout')
    
]
    
    
