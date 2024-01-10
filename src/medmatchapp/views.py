from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from medmatchapp.models import Patients

# Create your views here.

class PatientsListView(ListView):
    model = Patients
    
class PatientCreateView(CreateView):
    model = Patients
    fields = ["name", "gender", "date_of_birth", "contact_number", "address", "emergency_contact", "city", "medical_condition_description", "current_medications"]    