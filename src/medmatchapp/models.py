from django.db import models

# Create your models here.
class Patients(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    emergency_contact = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    medical_condition_description = models.TextField()
    current_medications = models.TextField()
    
    def get_absolute_url(self):
        return f"/medmatchapp/{self.id}/"
    
