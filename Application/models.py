from django.db import models

# Create your models here.
class Mydata(models.Model):
    Id=models.AutoField(primary_key=True)
    Fname=models.CharField(max_length=100)
    Lname=models.CharField(max_length=100)
    Gender=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    Phone_no=models.CharField(max_length=100)
    image=models.URLField()