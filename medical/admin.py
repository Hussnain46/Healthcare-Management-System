from django.contrib import admin

# Register your models here.
from .models import Prescription, MedicalRecord


admin.site.register(Prescription)
admin.site.register(MedicalRecord)