from rest_framework import serializers
from .models import Hostel, Level, Room, Bed


class SimpleBedSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='current_status', read_only=True)

    class Meta:
        model = Bed
        fields = ['id', 'status', 'bed_number']


class BedSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='current_status', read_only=True)
    room_id = serializers.IntegerField(source='room.id', read_only=True)
    room_number = serializers.CharField(source='room.number', read_only=True)
    level_id = serializers.IntegerField(source='room.level.id', read_only=True)
    level_number = serializers.IntegerField(source='room.level.number', read_only=True)
    hostel_id = serializers.IntegerField(source='room.level.hostel.id', read_only=True)
    hostel_name = serializers.CharField(source='room.level.hostel.name', read_only=True)

    class Meta:
        model = Bed
        fields = [
            'id',
            'status',
            'bed_number',
            'room_id',
            'room_number',
            'level_id',
            'level_number',
            'hostel_id',
            'hostel_name',
        ]


class RoomSerializer(serializers.ModelSerializer):
    beds = SimpleBedSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'number', 'capacity', 'beds']


class LevelSerializer(serializers.ModelSerializer):
    rooms = serializers.IntegerField(write_only=True)
    room_details = RoomSerializer(source='rooms', many=True, read_only=True)

    class Meta:
        model = Level
        fields = ['id', 'number', 'rooms', 'room_details']


class HostelSerializer(serializers.ModelSerializer):
    levels = LevelSerializer(many=True)
    capacity = serializers.IntegerField(write_only=True)

    class Meta:
        model = Hostel
        fields = ['id', 'name', 'gender', 'capacity', 'levels']

    def create(self, validated_data):
        levels_data = validated_data.pop('levels')
        capacity = validated_data.pop('capacity')
        hostel = Hostel.objects.create(**validated_data)

        for level_data in levels_data:
            num_rooms = level_data.pop('rooms')
            level = Level.objects.create(hostel=hostel, **level_data)

            # Create rooms and beds in bulk for better performance
            rooms = []
            beds = []

            for room_number in range(1, num_rooms + 1):
                room = Room(
                    level=level,
                    number=str(room_number).zfill(2),
                    capacity=capacity
                )
                rooms.append(room)

            # Bulk create rooms
            created_rooms = Room.objects.bulk_create(rooms)

            # Create beds for each room
            for room in created_rooms:
                for bed_number in range(1, capacity + 1):
                    bed = Bed(
                        room=room,
                        bed_number=str(bed_number).zfill(2),
                        status='available'
                    )
                    beds.append(bed)

            # Bulk create beds
            Bed.objects.bulk_create(beds)

        return hostel
