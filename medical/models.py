from django.db import models
from user.models import Doctor, Patient
from appointment.models import Appointment



class Prescription(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    instructions = models.TextField()

    def __str__(self):
        return f"Prescription {self.id} for Appointment {self.appointment.patient}"


class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Closed', 'Closed')])
    notes = models.TextField()
    record_date = models.DateField()

    def __str__(self):
        return f"Medical Record {self.id} for Patient {self.patient.username}"
