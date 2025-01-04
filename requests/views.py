from rest_framework import viewsets
from .models import MaintenanceRequest, ChangeRoomRequest
from .serializers import MaintenanceRequestSerializer, ChangeRoomRequestSerializer

class MaintenanceRequestViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer

    def patch(self, request, *args, **kwargs):
            instance = self.get_object()  # Get object based on 'id' from URL
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)

class ChangeRoomRequestViewSet(viewsets.ModelViewSet):
    queryset = ChangeRoomRequest.objects.all()
    serializer_class = ChangeRoomRequestSerializer


    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)