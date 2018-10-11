from django.db import models

# Create your models here.

class MyDB(models.Model):
    Name = models.CharField(max_length=30)
    Address=models.CharField(max_length=30)
    Roll = models.CharField(max_length = 15)
    Contact = models.CharField(max_length = 10)
    Available = models.BooleanField(default=0)
