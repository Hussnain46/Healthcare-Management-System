from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PatientRegistrationForm, DoctorRegistrationForm
from .models import Doctor, Patient
from appointment.models import Appointment

# Patient Registration View
class PatientRegisterView(CreateView):
    form_class = PatientRegistrationForm
    template_name = 'user/patient_register.html'
    success_url = reverse_lazy('patient_dashboard')

# Doctor Registration View
class DoctorRegisterView(CreateView):
    form_class = DoctorRegistrationForm
    template_name = 'user/doctor_register.html'
    success_url = reverse_lazy('doctor_dashboard')

# Patient Dashboard (only accessible after login)
class PatientDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'user/patient_dashboard.html'
    login_url = 'login'



# Doctor Dashboard (only accessible after login)
# Doctor dashboard view
class DoctorDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'user/doctor_dashboard.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appointments'] = Appointment.objects.filter(doctor=self.request.user.doctor)  # Update to filter appointments for the logged-in doctor
        return context
    

    

# Login View (shared between doctors and patients)
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm

class UserLoginView(LoginView):
    template_name = 'user/login.html'
    
    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)  # User ko login karein
        
        # Redirect based on user type
        if hasattr(user, 'patient'):
            return redirect('patient_dashboard')  # Patient dashboard URL name
        elif hasattr(user, 'doctor'):
            return redirect('doctor_dashboard')  # Doctor dashboard URL name
        
        return redirect('main_page')  # Default redirect


# Logout View
class UserLogoutView(LogoutView):
    next_page = 'main_page'


from django.views.generic import TemplateView

class MainPageView(TemplateView):
    template_name = 'user/main_page.html'
