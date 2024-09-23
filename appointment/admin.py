from django.contrib import admin

# Register your models here.

from .models import Appointment, AvailableDay, TimeSlot

admin.site.register(Appointment)
admin.site.register(AvailableDay)

class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ["id"]
admin.site.register(TimeSlot, TimeSlotAdmin)