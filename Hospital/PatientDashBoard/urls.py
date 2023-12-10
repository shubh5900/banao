
from django.urls import path
from . import views as Patient

urlpatterns = [
    path('Login/',Patient.LoginPage ),
    path('Registration/',Patient.RegistrationPage),
    path('Patient DashBoard/',Patient.PDashBoard),
]