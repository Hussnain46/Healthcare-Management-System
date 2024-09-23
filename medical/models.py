from django.db import models
from user.models import Doctor, Patient
from appointment.models import Appointment

class Prescription(models.Model):
    prescription_id = models.AutoField(primary_key=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    instructions = models.TextField()

    def __str__(self):
        return f"Prescription {self.prescription_id} for Appointment {self.appointment.appointment_id}"


class MedicalRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Closed', 'Closed')])
    notes = models.TextField()
    record_date = models.DateField()

    def __str__(self):
        return f"Medical Record {self.record_id} for Patient {self.patient.user.username}"
