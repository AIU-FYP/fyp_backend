from rest_framework import serializers
from .models import Hostel, Level, Room, Bed

class BedSerializer(serializers.ModelSerializer):

    id = serializers.CharField(source='bed_number')  # Using bed_number as the ID

    class Meta:
        model = Bed
        fields = ['id', 'status']

class RoomSerializer(serializers.ModelSerializer):
    beds = BedSerializer(many=True, read_only=True)  # Output beds in room
    class Meta:
        model = Room
        fields = ['number', 'capacity', 'beds']

class LevelSerializer(serializers.ModelSerializer):
    rooms = serializers.IntegerField(write_only=True)  # For input
    room_details = RoomSerializer(source='rooms', many=True, read_only=True)  # For output

    class Meta:
        model = Level
        fields = ['number', 'rooms', 'room_details']

class HostelSerializer(serializers.ModelSerializer):
    levels = LevelSerializer(many=True)
    capacity = serializers.IntegerField(write_only=True)  # Add capacity field

    class Meta:
        model = Hostel
        fields = ['name', 'gender', 'capacity', 'levels']

    def create(self, validated_data):
        levels_data = validated_data.pop('levels')
        capacity = validated_data.pop('capacity')  # Get the capacity
        hostel = Hostel.objects.create(**validated_data)

        for level_data in levels_data:
            num_rooms = level_data.pop('rooms')  # Get number of rooms needed
            level = Level.objects.create(hostel=hostel, **level_data)

            # Create rooms and beds
            for room_number in range(1, num_rooms + 1):
                room = Room.objects.create(
                    level=level,
                    number=str(room_number).zfill(2),  # Pad with zeros, e.g., "01", "02"
                    capacity=capacity
                )

                # Create beds for each room
                for bed_number in range(1, capacity + 1):  # Create beds based on room's capacity
                    Bed.objects.create(
                        room=room,
                        bed_number=str(bed_number).zfill(2),  # Bed ID format like "01", "02", etc.
                        status='available'  # Set status as 'available' by default
                    )

        return hostel

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['levels'] = sorted(
            representation['levels'],
            key=lambda x: x['number']
        )
        return representation
