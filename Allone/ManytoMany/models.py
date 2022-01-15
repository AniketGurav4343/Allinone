from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Song(models.Model):
    user = models.ManyToManyField(User)
    song_name = models.CharField(max_length=100)
    song_duration = models.IntegerField()

    def singed_by(self):
        return ",".join([str(p) for p in self.user.all()])

class classroom(models.Model):
    dept=models.CharField(max_length=100)
    subject= models.CharField(max_length=100)

class student(models.Model):
    clroom = models.ManyToManyField(classroom)
    sname =models.CharField(max_length=100)
    student_surname=models.CharField(max_length=100)

# c1 = classroom(dept="cs",subject="computer network")
# c1.save()

# c2.student_set.all()
# classroom.objects.get(id=1).student_set.all()
# student.objects.filter(clroom__id=1)
# student.objects.filter(clroom__pk=1)
# student.objects.filter(clroom=1)
# student.objects.filter(clroom=c1)
# student.objects.filter(clroom__dept__startswith="cs")
# student.objects.filter(clroom__dept__startswith="cs").distinct()
# student.objects.filter(clroom__dept__startswith="cs").count()
# student.objects.filter(clroom__dept__startswith="cs").distinct().count()
# student.objects.filter(clroom__in=[1,2]) 
# classroom.objects.filter(id=1)
# classroom.objects.filter(pk=1)
# classroom.objects.filter(student__sname_startswith="aniket") #############got error don't understand
# classroom.objects.filter(student__id=1)
# classroom.objects.filter(student__pk=1)
# classroom.objects.filter(student=1)
# classroom.objects.filter(student__in=[1,2]).distinct().count()
# classroom.objects.exclude(student=1)
#q = classroom.objects.filter(dept__startswith='cs')
#q.delete()
#s1 = student.objects.get(pk=1)
#c4.student.remove(s2)
# s2.classroom_set.remove(c5)
# s2.student_set.clear()