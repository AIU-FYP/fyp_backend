from rest_framework import viewsets
from .models import Hostel, Level, Room, Bed
from .serializers import HostelSerializer, LevelSerializer, RoomSerializer, BedSerializer

class HostelViewSet(viewsets.ModelViewSet):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer

    def get_queryset(self):
        return Hostel.objects.prefetch_related(
            'levels',
            'levels__rooms'
        )

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class BedViewSet(viewsets.ModelViewSet):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
