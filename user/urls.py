from django.urls import path
from user import views 





urlpatterns = [
    path('', views.MainPageView.as_view(), name='main_page'),
    path('patient-register/', views.PatientRegisterView.as_view(), name='patient_register'),
    path('doctor-register/', views.DoctorRegisterView.as_view(), name='doctor_register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('patient-dashboard/', views.PatientDashboardView.as_view(), name='patient_dashboard'),
    path('profile/', views.PatientProfileView.as_view(), name='patient_profile'),
    path('profile-update/', views.PatientProfileUpdateView.as_view(), name='patient_profile_update'),

    path('doctor-dashboard/', views.DoctorDashboardView.as_view(), name='doctor_dashboard'),
    path('doctor-profile/', views.DoctorProfileView.as_view(), name='doctor_profile'),
    path('doctor-p-update/', views.DoctorProfileUpdateView.as_view(), name='doctor_profile_update'),

    path('about/', views.AboutUsView.as_view(), name='about_us'),
    path('contact/', views.ContactFormView.as_view(), name='contact_us'),
    path('doctor/<int:pk>/', views.DoctorDetailView.as_view(), name='doctor_detail'),




    
]

