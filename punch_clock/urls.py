from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from punch_clock.views import *

router = routers.DefaultRouter()
router.register('functions', FunctionsViewSet)
router.register('employee', EmployeeViewSet)
router.register('attendance', AttendanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
