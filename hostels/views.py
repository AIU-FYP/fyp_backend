from rest_framework import viewsets
from .models import Hostel, Level, Room
from .serializers import HostelSerializer, LevelSerializer, RoomSerializer

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
