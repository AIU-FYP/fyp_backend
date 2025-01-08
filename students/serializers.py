from rest_framework import serializers

from hostels.serializers import BedSerializer
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    bed = BedSerializer()
    class Meta:
        model = Student
        fields = '__all__'