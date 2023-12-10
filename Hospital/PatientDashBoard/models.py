from django.db import models

# Create your models here.
class Patient(models.Model):
    FName=models.CharField(max_length=20)
    LName=models.CharField(max_length=20)
    Photo=models.FileField()
    Email=models.EmailField(max_length=100)
    UserName=models.CharField(max_length=100)
    Password=models.CharField(max_length=20)
    Local=models.CharField(max_length=20)
    City=models.CharField(max_length=20)
    Country=models.CharField(max_length=20)
    Pincode=models.CharField(max_length=7)
    def __str__(self):
        return f'{self.Email}'