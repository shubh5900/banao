
from django.urls import path
from . import views as Patient

urlpatterns = [
    path('LoginPage/',Patient.LoginPage ),
    path('RegistrationPage/',Patient.RegistrationPage),
    path('DashBoard/',Patient.DashBoard),
]