from django.views.generic import CreateView, ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import PrescriptionForm, MedicalRecordForm
from appointment.models import Appointment
from medical.models import Prescription, MedicalRecord
from user.models import Patient


class CreatePrescriptionView(CreateView):
    model = Prescription
    form_class = PrescriptionForm
    template_name = 'medical/create_prescription.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        appointment = get_object_or_404(Appointment, appointment_id=self.kwargs['appointment_id'])
        context['appointment'] = appointment
        return context

    def form_valid(self, form):
        appointment = get_object_or_404(Appointment, appointment_id=self.kwargs['appointment_id'])
        form.instance.appointment = appointment
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('confirmed_appointments')


class ViewPrescriptionView(DetailView):
    model = Prescription
    template_name = 'medical/view_prescriptions.html'
    context_object_name = 'prescription'

    def get_object(self):
        appointment_id = self.kwargs.get('appointment_id')
        appointment = get_object_or_404(Appointment, appointment_id=appointment_id)
        return get_object_or_404(Prescription, appointment=appointment)







class PatientPrescriptionsView(ListView):
    model = Prescription
    template_name = 'appointment/patient_prescriptions.html'
    context_object_name = 'prescriptions'

    def get_queryset(self):
        if self.request.user.is_authenticated and hasattr(self.request.user, 'patient'):
            return Prescription.objects.filter(appointment__patient=self.request.user.patient)
        return Prescription.objects.none() 
    



class PatientListView(ListView):
    model = Patient
    template_name = 'medical/patient_list.html'
    context_object_name = 'patients'

    def get_queryset(self):
        doctor = self.request.user.doctor
        return Patient.objects.filter(appointment__doctor=doctor).distinct()

class MedicalRecordCreateView(CreateView):
    model = MedicalRecord
    fields = ['prescription', 'status', 'notes', 'record_date']
    template_name = 'medical/create_medical_record.html'
    success_url = reverse_lazy('patient_list')


    def form_valid(self, form):
        form.instance.doctor = self.request.user.doctor
        patient = get_object_or_404(Patient, pk=self.kwargs['pk'])
        form.instance.patient = patient
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = get_object_or_404(Patient, pk=self.kwargs['pk'])
        return context

class MedicalRecordListView(ListView):
    model = MedicalRecord
    template_name = 'medical/medical_record_list.html'
    context_object_name = 'medical_records'

    def get_queryset(self):
        doctor = self.request.user.doctor  
        return MedicalRecord.objects.filter(doctor=doctor)
    

class PatientMedicalRecordListView(ListView):
    model = MedicalRecord
    template_name = 'medical/patient_record_list.html'
    context_object_name = 'medical_records'

    def get_queryset(self):
        patient = self.request.user.patient
        return MedicalRecord.objects.filter(patient=patient)