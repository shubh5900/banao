from django.shortcuts import render,redirect
from .models import Doctor
# Create your views here.
def LoginPage(request):
    if request.method=="POST":
        Email=request.POST["Email"]
        Password=request.POST["Password"]
        user=Doctor.objects.filter(Email=Email)
        print(user)
        #print(user.filter(Password==Password))
        if user.filter(Password=Password):
            return redirect("/Doctor/DashBoard/")
        else:
            message="Email or Password if wrong!"
            return render(request,"LoginPage.html", {"message":message})
    return render(request,"LoginPage.html")    

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
        Doctor(FName=fname,LName=lname,Photo=photo,Email=Email,Password=Password,Local=Line1,City=City,Country=Country,Pincode=Pincode).save()
        return redirect("/Doctor/LoginPage/")
    return render(request,"RegistrationPage.html")

def DashBoard(request):
    return render(request,"DashBoard.html")