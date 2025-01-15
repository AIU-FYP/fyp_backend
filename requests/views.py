from rest_framework import viewsets
from rest_framework.response import Response
from django.conf import settings

from .models import MaintenanceRequest, ChangeRoomRequest
from .serializers import MaintenanceRequestSerializer, ChangeRoomRequestSerializer

from utils.emails import (
    send_change_room_request_created,
    send_change_room_request_update,
    send_maintenance_request_created,
    send_maintenance_request_update
)

SA_EMAIL = settings.STAFF_EMAIL
PPK_EMAIL = settings.PPK_EMAIL


class ChangeRoomRequestViewSet(viewsets.ModelViewSet):
    queryset = ChangeRoomRequest.objects.all()
    serializer_class = ChangeRoomRequestSerializer

    def perform_create(self, serializer):
        request = serializer.save()
        send_change_room_request_created(
            request,
            request.email,
            SA_EMAIL
        )

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            updated_instance = serializer.save()
            send_change_room_request_update(updated_instance, updated_instance.email)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class MaintenanceRequestViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer

    def perform_create(self, serializer):
        request = serializer.save()
        send_maintenance_request_created(
            request,
            request.email,
            SA_EMAIL,
            PPK_EMAIL
        )

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            send_maintenance_request_update(
                request,
                request.email,
                SA_EMAIL
            )
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
