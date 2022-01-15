from django.db import models
#for authenticatin and permision


# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    salary=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', related_name='books', on_delete=models.CASCADE)
    highlighted = models.TextField()

    def __str__(self):
        return self.name

