from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator,RegexValidator   
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.exceptions import ValidationError
 
 

# Create your models here.
class User(AbstractUser):

    pass 
class specialty(models.Model):
    name=models.CharField(max_length=255)    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    Doctors=models.ManyToManyField('Doctor',related_name='specialties')

class Doctor(User):
    license_number=models.CharField(max_length=6 ,unique=true ,validators=[MinLengthValidator(6)])
    phone=models.CharField(max_length=8)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    specialities=models.ManyToManyField('specialty',related_name='doctors')
    specialty,
    related_name='doctors',
number_validator= RegexValidator(regex=r'^\d{6}$', message='License number must be exactly 6 digits.')  
def validate_birth_date(v):
    if v > timezone.localdate().date():
        raise ValidationError('ne pas valide ')
#specialty=models.ForeignKey('specialty', on_delete=models.CASCADE, related_name="doctors")
class patient(user):
    national_id=models.CharField(max_length=8,unique=true,validators=[MinLengthValidator(8), number_validator])
    phone=models.CharField(max_length=8,validators=[number_validator])
    birth_date=models.DateField(validators=[validate_birth_date])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

