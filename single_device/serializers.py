from rest_framework import serializers

from single_device.models import StaffLogin


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model=StaffLogin
        fields='__all__'
        read_only_fields=('id',)
