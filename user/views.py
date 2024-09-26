from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView, UpdateView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from .forms import PatientRegistrationForm, DoctorRegistrationForm, PatientUpdateForm, DoctorUpdateForm
from .models import Doctor, Patient
from appointment.models import Appointment


class PatientRegisterView(CreateView):
    form_class = PatientRegistrationForm
    template_name = 'user/patient_register.html'
    success_url = reverse_lazy('patient_dashboard')


class PatientDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'user/patient_dashboard.html'
    login_url = 'login'


class PatientProfileView(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = 'user/patient_profile.html'

    def get_object(self):
        return self.request.user.patient


class PatientProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Patient
    form_class = PatientUpdateForm
    template_name = 'user/patient_profile_update.html'
    success_url = reverse_lazy('patient_profile')

    def get_object(self):
        return self.request.user.patient


class DoctorRegisterView(CreateView):
    form_class = DoctorRegistrationForm
    template_name = 'user/doctor_register.html'
    success_url = reverse_lazy('doctor_dashboard')


class DoctorProfileView(LoginRequiredMixin, DetailView):
    model = Doctor
    template_name = 'user/doctor_profile.html'

    def get_object(self):
        return self.request.user.doctor


class DoctorProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Doctor
    form_class = DoctorUpdateForm
    template_name = 'user/doctor_profile_update.html'
    success_url = reverse_lazy('doctor_profile')

    def get_object(self):
        return self.request.user.doctor


class DoctorDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'user/doctor_dashboard.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appointments'] = Appointment.objects.filter(doctor=self.request.user.doctor, status='confirmed')
        return context


class UserLoginView(LoginView):
    template_name = 'user/login.html'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        
        if hasattr(user, 'patient'):
            return redirect('patient_dashboard')
        elif hasattr(user, 'doctor'):
            return redirect('doctor_dashboard')
        
        return redirect('main_page')


class UserLogoutView(LogoutView):
    next_page = 'main_page'


class MainPageView(TemplateView):
    template_name = 'user/main_page.html'

