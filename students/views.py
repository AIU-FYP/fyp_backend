from rest_framework import viewsets

from rest_framework.response import Response
from utils.emails import send_student_welcome_email
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.select_related(
            'bed',
            'bed__room',
            'bed__room__level',
            'bed__room__level__hostel'
        )

    def partial_update(self, request, *args, **kwargs):
        student = self.get_object()

        if 'status' in request.data:
            new_status = request.data['status']

            if new_status not in ['active', 'internship']:
                request.data['bed'] = None


        serializer = self.get_serializer(
            student,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
