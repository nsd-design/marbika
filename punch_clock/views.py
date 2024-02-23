from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class FunctionsViewSet(viewsets.ModelViewSet):
    queryset = Functions.objects.all()
    serializer_class = FunctionsSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

