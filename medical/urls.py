from django.urls import path
from .views import (
    CreatePrescriptionView,
    ViewPrescriptionView,
    PatientPrescriptionsView,
    PatientListView,
    MedicalRecordCreateView,
    MedicalRecordListView,
    PatientMedicalRecordListView
    
    
    )

urlpatterns = [
    path('create-prescription/<int:appointment_id>/', CreatePrescriptionView.as_view(), name='create_prescription'),
    path('view-prescriptions/<int:appointment_id>/', ViewPrescriptionView.as_view(), name='view_specific_prescription'),
    
    path('patient_prescriptions/', PatientPrescriptionsView.as_view(), name='patient_prescriptions'),


    path('patients/', PatientListView.as_view(), name='patient_list'),
    path('patient/<int:pk>/medical-record/', MedicalRecordCreateView.as_view(), name='create_medical_record'),
    path('doctor/medical-records/', MedicalRecordListView.as_view(), name='medical_record_list'),


    path('medical-records/', PatientMedicalRecordListView.as_view(), name='patient_medical_record_list'),



    




]