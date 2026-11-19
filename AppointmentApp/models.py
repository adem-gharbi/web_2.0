from django.db import models
from AccountApp.models import Doctor, patient

class Appointment(models.Model):
    reason =models.TextField()
    prescription=models.FileField(blank=True, upload_to='prescriptions/')

    class status(models.TextChoices):
        PENDING = 'pending',"en attente"
        CONFIRMED = 'confirmed'
        CANCELLED = 'annulé'
        status=models.CharField(max_length=10,choices=status.choices,default=status.PENDING)    
        duration_minutes=models.PositiveIntegerField(default=30)
        created_at=models.DateTimeField(auto_now_add=True)
        updated_at=models.DateTimeField(auto_now=True)
        appointment_date=models.DateTimeField()
        Doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='appointments')
        patient=models.ForeignKey(patient,on_delete=models.CASCADE,related_name='appointments')