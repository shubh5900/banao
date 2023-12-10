from django.shortcuts import render,redirect
from .models import Patient
# Create your views here.
def LoginPage(request):
    if request.method=="POST":
        Email=request.POST["Email"]
        Password=request.POST["Password"]
        user=Patient.objects.filter(Email=Email)
        print(user)
        if user.filter(Password=Password):
            return redirect("/Patient/DashBoard/")
        else:
            message="Email or Password if wrong!"
            return render(request,"Login.html", {"message":message})
    return render(request,"Login.html")   

    #return render(request,"Patient/LoginPage.html")

def RegistrationPage(request):
    if request.method=="POST":
        fname=request.POST["FirstName"]
        lname=request.POST["LastName"]
        photo=request.POST["Photo"]
        Email=request.POST["Email"]
        Password=request.POST["Password"]
        Line1=request.POST["Line1"]
        City=request.POST["City"]
        Country=request.POST["Country"]
        Pincode=request.POST["Pincode"]
        Patient(FName=fname,LName=lname,Photo=photo,Email=Email,Password=Password,Local=Line1,City=City,Country=Country,Pincode=Pincode).save()
        return redirect("/Patient/Login/")
    return render(request,"Registration.html")
def PDashBoard(request):
    return render(request,"PDashBoard.html")