# Generated by Django 3.1.2 on 2022-01-10 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManytoMany', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('student_surname', models.CharField(max_length=100)),
                ('clroom', models.ManyToManyField(to='ManytoMany.classroom')),
            ],
        ),
    ]
