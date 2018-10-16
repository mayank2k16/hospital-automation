from django.urls import path
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('doctors',views.doctors, name = 'doctors'), 
    path('api/receive_incoming_patient',views.receive_patient, name = 'incoming_patient'),
    path('reception', views.reception, name = "reception"),
    path('reception/ajax/<int:id>', views.autocomplete, name="autocomplete"),
    path('doctor/<int:patient_id>',views.prescriptions,name="prescriptions"),
]

