from rest_framework import viewsets
from .models import Hostel, Level, Room, Bed
from .serializers import HostelSerializer, LevelSerializer, RoomSerializer, BedSerializer
from django.db import models
from rest_framework.decorators import action
from rest_framework.response import Response
from students.models import Student
from requests.models import MaintenanceRequest, ChangeRoomRequest

class HostelViewSet(viewsets.ModelViewSet):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer

    def get_queryset(self):
        return Hostel.objects.prefetch_related(
            'levels',
            'levels__rooms'
        )

    @action(detail=False, methods=['get'])
    def stats(self, request):
        student_stats = Student.objects.aggregate(
            total_male=models.Count('id', filter=models.Q(gender='male')),
            total_female=models.Count('id', filter=models.Q(gender='female')),
        )

        # Get room occupancy statistics
        total_capacity = Room.objects.aggregate(
            total_capacity=models.Sum('capacity')
        )['total_capacity'] or 0

        occupied_beds = Student.objects.filter(
            status='active'
        ).count()

        available_beds = total_capacity - occupied_beds if total_capacity > occupied_beds else 0

        # Get request statistics
        maintenance_requests = MaintenanceRequest.objects.count()
        change_room_requests = ChangeRoomRequest.objects.count()

        # Total rooms and hostels statistics
        total_hostels = Hostel.objects.count()
        total_rooms = Room.objects.count()

        stats = {
            'student_statistics': {
                'male_students': student_stats['total_male'],
                'female_students': student_stats['total_female'],
                'total_students': student_stats['total_male'] + student_stats['total_female']
            },
            'occupancy_statistics': {
                'total_capacity': total_capacity,
                'occupied_beds': occupied_beds,
                'available_beds': available_beds,
                'occupancy_rate': round((occupied_beds / total_capacity * 100), 2) if total_capacity > 0 else 0
            },
            'request_statistics': {
                'maintenance_requests': maintenance_requests,
                'change_room_requests': change_room_requests,
                'total_requests': maintenance_requests + change_room_requests
            },
            'hostel_statistics': {
                'total_hostels': total_hostels,
                'total_rooms': total_rooms
            }
        }

        return Response(stats)

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class BedViewSet(viewsets.ModelViewSet):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
