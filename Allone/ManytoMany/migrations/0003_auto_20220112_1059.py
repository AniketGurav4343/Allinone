# Generated by Django 3.1.2 on 2022-01-12 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManytoMany', '0002_classroom_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_name',
            new_name='sname',
        ),
    ]