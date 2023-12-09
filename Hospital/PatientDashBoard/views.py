from django.shortcuts import render

# Create your views here.
def LoginPage(request):
    return render(request,"Patient/LoginPage.html")

def RegistrationPage(request):
    return render(request,"Patient/RegistrationPage.html")

def DashBoard(request):
    return render(request,"DashBoard.html")