from rest_framework import serializers
from .models import *


class FunctionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Functions
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
