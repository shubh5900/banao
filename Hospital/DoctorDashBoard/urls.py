
from django.urls import path
from . import views

urlpatterns = [
    
    path('RegistrationPage/',views.RegistrationPage),
    path('DashBoard/',views.DashBoard),
    path('LoginPage/',views.LoginPage),
]