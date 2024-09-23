from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Patient, Doctor, User

class DoctorRegistrationForm(UserCreationForm):
    class Meta:
        model = Doctor
        fields = ['username', 'first_name', 'last_name', 'email', 'CNIC_no', 'contact_number', 'address', 'gender', 'specialization', 'license_number', 'qualification', 'experience', 'consultation_fee']


class PatientRegistrationForm(UserCreationForm):
    class Meta:
        model = Patient
        fields = ['username', 'first_name', 'last_name', 'email', 'CNIC_no', 'contact_number', 'address', 'gender', 'date_of_birth', 'blood_group', 'marital_status', 'emergency_contact']
    
    def __init__(self, *args, **kwargs):
        super(PatientRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''