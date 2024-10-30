from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import logout
from django.views.generic import ListView, TemplateView, FormView, UpdateView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.utils.timezone import datetime, timedelta
from datetime import date
from .models import Appointment, AvailableDay, TimeSlot
from medical.models import MedicalRecord
from .forms import AppointmentForm, AvailabilityForm, UpdateAvailabilityForm
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist






class AppointmentStatusView(TemplateView):
    template_name = 'appointment/appointment_status.html'

    def get_context_data(self, **kwargs):
        context = super(AppointmentStatusView, self).get_context_data(**kwargs)
        appointment = Appointment.objects.get(pk=self.kwargs['pk'])
        context['appointment'] = appointment
        return context


class DoctorAvailabilityView(LoginRequiredMixin, FormView):
    template_name = 'appointment/set_availability.html'
    form_class = AvailabilityForm
    success_url = reverse_lazy('doctor_dashboard')

    def form_valid(self, form):
        available_days = form.cleaned_data['available_days']
        start_time = form.cleaned_data['start_time']
        end_time = form.cleaned_data['end_time']

        doctor = self.request.user.doctor

        for day in available_days:
            available_day, created = AvailableDay.objects.get_or_create(doctor=doctor, day=day)

            TimeSlot.objects.filter(doctor=doctor, day=available_day).delete()
            
            current_time = start_time
            while current_time < end_time:
                TimeSlot.objects.create(doctor=doctor, day=available_day, time=current_time)
                current_time = (datetime.combine(date.today(), current_time) + timedelta(minutes=30)).time()

        return super().form_valid(form)



class BookAppointmentView(LoginRequiredMixin, FormView):
    template_name = 'appointment/book_appointment.html'
    form_class = AppointmentForm

    def dispatch(self, request, *args, **kwargs):
        # Check if the logged-in user is a Patient
        if not hasattr(request.user, 'patient'):
            # Logout the user and redirect them to the login page if they are not a Patient
            logout(request)
            return redirect(reverse_lazy('login'))

        return super().dispatch(request, *args, **kwargs)


    def form_valid(self, form):
        doctor = form.cleaned_data['doctor']
        day = form.cleaned_data['day']
        time = form.cleaned_data['time']
        Appointment.objects.create(
            patient=self.request.user.patient,
            doctor=doctor,
            time_slot=time
        )
        return redirect('view_booked_appointments')
    


class DoctorAppointmentsView(ListView):
    model = Appointment
    template_name = 'doctor/appointments.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        return Appointment.objects.filter(doctor=self.request.user.doctor)


class ViewBookedAppointmentsView(LoginRequiredMixin, ListView):
    template_name = 'appointment/view_booked_appointments.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        return Appointment.objects.filter(patient=self.request.user.patient).order_by('-appointment_date')

    
class AppointmentRequestListView(LoginRequiredMixin, ListView):
    template_name = 'appointment/appointment_requests.html'
    model = Appointment
    context_object_name = 'appointments'


    def get_queryset(self):
        return Appointment.objects.filter(doctor=self.request.user.doctor, status='Pending')



class ConfirmAppointmentView(View):
    def post(self, request, appointment_id):
        appointment = get_object_or_404(Appointment, appointment_id=appointment_id)

        # Check if the logged-in user is the doctor for this appointment
        if appointment.doctor == request.user.doctor:
            appointment.status = 'Confirmed'
            appointment.save()
            messages.success(request, 'Appointment confirmed successfully!')

            # Fetch the latest active medical record for the patient
            medical_record = MedicalRecord.objects.filter(patient=appointment.patient, status='Active').last()
            if medical_record:
                messages.info(request, f'Latest Medical Record: {medical_record.notes}')  
            else:
                messages.info(request, 'No active medical record found for this patient.')

        else:
            messages.error(request, 'You do not have permission to confirm this appointment.')

        return redirect('view_appointment_requests')


class ConfirmedAppointmentsView(ListView):
    model = Appointment
    template_name = 'appointment/confirmed_appointments.html'
    context_object_name = 'confirmed_appointments'

    def get_queryset(self):
        try:
            return Appointment.objects.filter(doctor=self.request.user.doctor, status='Confirmed').prefetch_related('prescription')
        except ObjectDoesNotExist:
            return redirect('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    



class GetAvailableDays(View):
    def get(self, request, *args, **kwargs):
        doctor_id = request.GET.get('doctor_id')
        if doctor_id:
            available_days = AvailableDay.objects.filter(doctor_id=doctor_id).values('id', 'day')
            return JsonResponse(list(available_days), safe=False)
        return JsonResponse({'error': 'No doctor selected'}, status=400)


class GetAvailableTimeSlots(View):
    def get(self, request, *args, **kwargs):
        day_id = request.GET.get('day_id')
        if day_id:
            time_slots = TimeSlot.objects.filter(day_id=day_id).values('id', 'time')
            return JsonResponse(list(time_slots), safe=False)
        return JsonResponse({'error': 'No day selected'}, status=400)


class DoctorTimetableView(LoginRequiredMixin, ListView):
    template_name = 'appointment/view_timetable.html'
    model = AvailableDay

    def get_queryset(self):
        return AvailableDay.objects.filter(doctor=self.request.user.doctor)


class UpdateAvailabilityView(UpdateView):
    model = AvailableDay
    form_class = UpdateAvailabilityForm
    template_name = 'appointment/update_availability.html'
    success_url = reverse_lazy('view_timetable')

    def get_queryset(self):
        return AvailableDay.objects.filter(doctor=self.request.user.doctor)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['day'] = self.get_object()
        context['time_slots'] = TimeSlot.objects.filter(day=context['day']).exclude(
            doctor=self.request.user.doctor,
            appointment__time_slot__day=context['day']
        ).distinct()
        return context


def remove_time_slot(request, time_slot_id):
    time_slot = get_object_or_404(TimeSlot, id=time_slot_id)
    if request.method == 'POST':
        time_slot.delete()
        return redirect('view_timetable')
    return render(request, 'appointment/remove_time_slot.html', {'time_slot': time_slot})
