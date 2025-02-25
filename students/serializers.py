from rest_framework import serializers

from hostels.models import Bed
from hostels.serializers import BedSerializer, SimpleBedSerializer
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    bed_id = serializers.IntegerField(source='bed.id', read_only=True)
    bed_number = serializers.CharField(source='bed.bed_number', read_only=True)
    bed_status = serializers.CharField(source='bed.current_status', read_only=True)
    room_id = serializers.IntegerField(source='bed.room.id', read_only=True)
    room_number = serializers.CharField(source='bed.room.number', read_only=True)
    level_id = serializers.IntegerField(source='bed.room.level.id', read_only=True)
    level_number = serializers.IntegerField(source='bed.room.level.number', read_only=True)
    hostel_id = serializers.IntegerField(source='bed.room.level.hostel.id', read_only=True)
    hostel_name = serializers.CharField(source='bed.room.level.hostel.name', read_only=True)

    bed = serializers.PrimaryKeyRelatedField(
        queryset=Bed.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Student
        fields = [
            'id',
            'name',
            'student_id',
            'passport',
            'arrival_date',
            'phone',
            'email',
            'gender',
            'religion',
            'nationality',
            'major',
            'status',
            'bed',
            'bed_id',
            'bed_number',
            'bed_status',
            'room_id',
            'room_number',
            'level_id',
            'level_number',
            'hostel_id',
            'hostel_name',
        ]

    def validate_bed(self, value):
        if value:
            # Check if bed is available
            if value.current_status != 'available':
                raise serializers.ValidationError("This bed is not available")

            # Get gender from initial data for creation or instance for updates
            student_gender = self.initial_data.get('gender') if not self.instance else self.instance.gender

            # Check if gender matches hostel gender
            if value.room.level.hostel.gender != student_gender:
                raise serializers.ValidationError(
                    "Student gender doesn't match hostel gender"
                )
        return value

    def validate(self, attrs):
        # Remove unnecessary fields that might come from frontend
        attrs.pop('block_name', None)
        attrs.pop('level_number', None)
        attrs.pop('room', None)
        attrs.pop('Date', None)
        return attrs
