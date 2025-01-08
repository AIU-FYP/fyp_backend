from rest_framework import viewsets

from utils.emails import send_student_welcome_email
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.select_related(
            'bed',
            'bed__room',
            'bed__room__level',
            'bed__room__level__hostel'
        )

    def perform_create(self, serializer):
        student = serializer.save()
        send_student_welcome_email(student)
