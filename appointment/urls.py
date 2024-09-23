from django.urls import path
from .views import (
    AppointmentStatusView,
    BookAppointmentView,
    DoctorAvailabilityView,
    DoctorTimetableView,
    UpdateAvailabilityView, 
    remove_time_slot,
    GetAvailableDays,
    GetAvailableTimeSlots, 
    ConfirmAppointmentView, ViewBookedAppointmentsView, 
)

urlpatterns = [
    path('status/<int:pk>/', AppointmentStatusView.as_view(), name='appointment_status'),
    path('book/', BookAppointmentView.as_view(), name='book_appointment'),
    path('availability/', DoctorAvailabilityView.as_view(), name='set_availability'),
    path('timetable/', DoctorTimetableView.as_view(), name='view_timetable'),
    path('availability/update/<int:pk>/', UpdateAvailabilityView.as_view(), name='update_availability'),
    path('remove_time_slot/<int:time_slot_id>/', remove_time_slot, name='remove_time_slot'),
    path('ajax/get_available_days/', GetAvailableDays.as_view(), name='get_available_days'),
    path('ajax/get_available_time_slots/', GetAvailableTimeSlots.as_view(), name='get_available_time_slots'),
    path('confirm_appointment/<int:appointment_id>/', ConfirmAppointmentView.as_view(), name='confirm_appointment'),
    path('view/', ViewBookedAppointmentsView.as_view(), name='view_booked_appointments'),




    
]



