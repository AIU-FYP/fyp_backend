from rest_framework import viewsets

from django.apps import apps
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
            total_active=models.Count('id', filter=models.Q(status='active')),
            total_inactive=models.Count('id', filter=models.Q(status='inactive')),
            total_graduated=models.Count('id', filter=models.Q(status='graduated')),
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
                'total_students': student_stats['total_male'] + student_stats['total_female'],
                'total_active': student_stats['total_active'],
                'total_inactive': student_stats['total_inactive'],
                'total_graduated': student_stats['total_graduated'],
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

    def get_queryset(self):
        return Bed.objects.select_related(
            'room',
            'room__level',
            'room__level__hostel'
        )

    def partial_update(self, request, *args, **kwargs):
        bed = self.get_object()

        if request.data.get('status') == 'under_maintenance':
            Student = apps.get_model('students', 'Student')
            if Student.objects.filter(bed=bed, status='active').exists():
                return Response(
                    {"error": "Cannot set bed to maintenance while occupied by an active student"},
                    status=400
                )

        serializer = self.get_serializer(bed, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
