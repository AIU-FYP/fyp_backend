from rest_framework import viewsets
from .models import MaintenanceRequest, ChangeRoomRequest
from .serializers import MaintenanceRequestSerializer, ChangeRoomRequestSerializer

class MaintenanceRequestViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer

class ChangeRoomRequestViewSet(viewsets.ModelViewSet):
    queryset = ChangeRoomRequest.objects.all()
    serializer_class = ChangeRoomRequestSerializer
