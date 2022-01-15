from pyexpat import model
from django.db import models

# Create your models here.
class CommandEmployee(models.Model):
    name=models.CharField(max_length=100)
    region = models.CharField(max_length=2, choices=[('NA','North America'),('EU','Europe')])
    moderator= models.BooleanField()
    
    def __str__(self):
        return self.name