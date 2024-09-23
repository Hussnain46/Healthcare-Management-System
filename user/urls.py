from django.urls import path
from user import views 



urlpatterns = [
    path('', views.MainPageView.as_view(), name='main_page'),
    path('patient-register/', views.PatientRegisterView.as_view(), name='patient_register'),
    path('doctor-register/', views.DoctorRegisterView.as_view(), name='doctor_register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('patient-dashboard/', views.PatientDashboardView.as_view(), name='patient_dashboard'),
    path('doctor-dashboard/', views.DoctorDashboardView.as_view(), name='doctor_dashboard'),
    
]
