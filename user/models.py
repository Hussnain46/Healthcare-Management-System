from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    CNIC_no = models.CharField(max_length=15, unique=True)
    contact_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
    profile_pic = models.ImageField(upload_to='images/profile_pics/', blank=True, null=True)


    def __str__(self):
        return self.username



class Doctor(User):
    specialization = models.CharField(max_length=255)
    license_number = models.CharField(max_length=50, unique=True)
    qualification = models.CharField(max_length=255)
    experience = models.IntegerField()
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Doctor'

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"


class Patient(User):
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=3)
    marital_status = models.CharField(max_length=10, choices=[('Single', 'Single'), ('Married', 'Married')])
    emergency_contact = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Patient'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
