from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.generic import ListView, TemplateView, FormView, UpdateView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.utils.timezone import datetime, timedelta
from datetime import date
from .models import Appointment, AvailableDay, TimeSlot
from .forms import AppointmentForm, AvailabilityForm, UpdateAvailabilityForm



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
            available_days = AvailableDay.objects.filter(doctor=doctor, day=day)

            if available_days.exists():
                available_day = available_days.first()
                available_days.exclude(id=available_day.id).delete()
            else:
                available_day = AvailableDay.objects.create(doctor=doctor, day=day)

            current_time = start_time
            while current_time < end_time:
                if not TimeSlot.objects.filter(doctor=doctor, day=available_day, time=current_time).exists():
                    TimeSlot.objects.create(doctor=doctor, day=available_day, time=current_time)
                current_time = (datetime.combine(date.today(), current_time) + timedelta(minutes=30)).time()

        return super().form_valid(form)


class BookAppointmentView(LoginRequiredMixin, FormView):
    template_name = 'appointment/book_appointment.html'
    form_class = AppointmentForm

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
        return Appointment.objects.filter(patient=self.request.user.patient)


class ViewDoctorAppointmentsView(ListView):
    model = Appointment
    template_name = 'doctor/view_appointments.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        return Appointment.objects.filter(doctor=self.request.user.doctor, status='Pending')


class ConfirmAppointmentView(View):
    def post(self, request, appointment_id):
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.status = 'Confirmed'
        appointment.save()
        return redirect('view_doctor_appointments')


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
