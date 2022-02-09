from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Profile(models.Model):
   name = models.CharField(max_length=100)
   rollno = models.CharField(max_length = 100)
   

