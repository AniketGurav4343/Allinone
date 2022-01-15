from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=100)
    salary=models.ImageField()

    def __str__(self):
        return self.name
#*********************** vlaues ********************
#Author.objects.values() ############ values give data in dictionary format
#<QuerySet [{'id': 1, 'name': 'aniket', 'salary': '600000'}, {'id': 2, 'name': 'ram', 'salary': '580000'}, {'id': 3, 'name': 'sham', 'salary': '300000'}, {'id': 4, 'name': 'sona', 'salary': '350000'}, {'id': 5, 'name': 'swagati', 'salary': '950000'}, {'id': 6, 'name': 'swati', 'salary': '150000'}, {'id': 7, 'name': 'soniya', 'salary': '1500000'}, {'id': 8, 'name': 'shailesh', 'salary': '390000'}]>
# print(Author.objects.values('id','name').query)

# Author.objects.filter(name__contains="an").values('id','name')
# <QuerySet [{'id': 1, 'name': 'aniket'}]>

# Author.objects.values('id','Course__name') ##access the value of foreignkey table values
#Author.objects.filter(Course__name_containd='cs').values('id','Course__name')

#*********************** vlaues_list ********************
# Author.objects.values_list('id') ######### values_list give data in tuple format
# <QuerySet [(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,)]>

# Author.objects.values_list('id', named=True)

# Author.objects.values_list('id', flat=True)
# <QuerySet [1, 2, 3, 4, 5, 6, 7, 8]>

# ids = Author.objects.values_list('id', flat=True)
# ids.filter(salary__gt=300000)
# <QuerySet [1, 2, 4, 5, 8]>
