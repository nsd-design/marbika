
from django.contrib.auth.models import User
from django.db import models


class Functions(models.Model):
    function = models.CharField(max_length=100)

    def __str__(self):
        return self.function


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    badge = models.CharField(max_length=12, unique=True)
    function_employee = models.ForeignKey(Functions, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.badge}"


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    check_in_time = models.DateTimeField()
    check_out_time = models.DateTimeField(null=True, blank=True)
    status = models.SmallIntegerField(choices=[(1, "IN"), (0, "OUT")])

    def __str__(self):
        return f"{self.employee.user.get_full_name()} - IN: {self.check_in_time} - OUT: {self.check_out_time}"

