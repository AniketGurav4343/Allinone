from rest_framework import serializers
from rest_framework import fields
from .models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
        fields = '__all__'
        