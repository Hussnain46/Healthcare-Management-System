from django.db import models
from user.models import Doctor, Patient

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField(null=True)
    appointment_time = models.TimeField(null=True) 
    time_slot = models.ForeignKey('TimeSlot', null=True, blank=True, on_delete=models.SET_NULL)  # Link to TimeSlot
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Rescheduled', 'Rescheduled')], default='Pending')

    def __str__(self):
        return f"Appointment {self.appointment_id} - {self.status}"



class AvailableDay(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day = models.CharField(max_length=9)

    def __str__(self):
        return f"{self.doctor}'s availability on {self.day}"

class TimeSlot(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day = models.ForeignKey(AvailableDay, on_delete=models.CASCADE)
    time = models.TimeField()

    def __str__(self):
        return f"{self.doctor} - {self.time}"
