from django.db import models


# Create your models here.
class Profile(models.Model):
   name = models.CharField(max_length=100)
   rollno = models.CharField(max_length = 100)
   # images = models.FileField(blank=True)

# class profileImages(models.Model):
       
   

