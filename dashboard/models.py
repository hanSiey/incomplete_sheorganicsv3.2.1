from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Distributor(models.Model):
     STATUS = (
        ('Active', 'Active'),
        ('Not Available', 'Not Available'),
     )
     name = models.CharField(max_length=20)
     surname = models.CharField(max_length=20, null=True)
     phone = models.CharField(max_length=15, null=True)
     email = models.EmailField()
     area_of_operation = models.CharField(max_length=200)
     status = models.CharField(max_length=20, null=True, blank=True, choices=STATUS, default="Active") 
     def __str__(self):
         return self.name

class OnlineContact(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.CharField(max_length=1000)
    date_sent = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name