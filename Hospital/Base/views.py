from django.shortcuts import render,redirect
from DoctorDashBoard.models import Doctor
# Create your views here.
def Base(request):
    return render(request,"Base.html")