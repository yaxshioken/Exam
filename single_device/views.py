from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from single_device.models import StaffLogin
from single_device.serializers import DeviceSerializer


class DeviceViewSet(ModelViewSet):
    serializer_class = DeviceSerializer
    queryset = StaffLogin.objects.all()
