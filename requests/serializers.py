from rest_framework import serializers
from .models import MaintenanceRequest, ChangeRoomRequest

class MaintenanceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRequest
        fields = '__all__'

class ChangeRoomRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChangeRoomRequest
        fields = '__all__'
