from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    name =models.CharField(max_length=100)
    author=models.ForeignKey(Author,on_delete=CASCADE,related_name='course')
    
    def __str__(self):
        return self.name


#Course.objects.all() # if we want all the object and only id
#Course.objects.select_related() # if we want inner join and object form foreignkey table to other table
#Course.objects.prefetch_related() # if data form other tabel to foreignkey table 

#Course.objects.all()[0].author
#Course.objects.select_related()[0].author
#Course.objects.prefetch_related()[0].author

#Author.objects.all('course') #error
#Author.objects.select_related('course') #error
#Author.objects.prefetch_related('course')