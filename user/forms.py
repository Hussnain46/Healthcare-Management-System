from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Patient, Doctor, User

class DoctorRegistrationForm(UserCreationForm):
    class Meta:
        model = Doctor
        fields = ['username', 'first_name', 'last_name', 
                  'email', 'CNIC_no', 'contact_number', 
                  'address', 'gender', 'specialization', 
                  'license_number', 'qualification', 
                  'experience', 'consultation_fee', 'profile_pic']

    def __init__(self, *args, **kwargs):
        super(DoctorRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

class DoctorUpdateForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['specialization', 'license_number', 
                  'qualification', 'experience', 'consultation_fee', 'profile_pic']


class PatientRegistrationForm(UserCreationForm):
    class Meta:
        model = Patient
        fields = ['username', 
                  'first_name', 
                  'last_name', 
                  'email', 
                  'CNIC_no', 
                  'contact_number', 
                  'address', 
                  'gender', 
                  'date_of_birth', 
                  'blood_group', 
                  'marital_status', 
                  'emergency_contact', 
                  'profile_pic'
                  ]
        
        widgets = {
            'date_of_birth': forms.DateInput(attrs={
                'type': 'date',  # HTML5 date picker
                'class': 'form-control',  # Optional: add Bootstrap class for styling
                'placeholder': 'Select your birth date'  # Optional: placeholder text
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super(PatientRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

        



class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['contact_number', 'address', 'date_of_birth', 'blood_group', 'emergency_contact', 'profile_pic']

