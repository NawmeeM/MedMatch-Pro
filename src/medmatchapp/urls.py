#cloud_journey/src/pets/urls.py
from django.urls import path
from medmatchapp.views import PatientsListView, PatientCreateView

urlpatterns = [
    path("all/", PatientsListView.as_view(), name="patient-list"),
    path("add/", PatientCreateView.as_view(), name="add-patient"),
    
]
