from rest_framework import serializers
from .models import Hostel, Level, Room, Bed

class BedSerializer(serializers.ModelSerializer):

    id = serializers.CharField(source='bed_number')  # Using bed_number as the ID

    class Meta:
        model = Bed
        fields = ['id', 'status', 'bed_number']

    def update(self, instance, validated_data):
            instance.status = validated_data.get('status', instance.status)
            instance.save()
            return instance

class RoomSerializer(serializers.ModelSerializer):
    beds = BedSerializer(many=True, read_only=True)
    class Meta:

        model = Room
        fields = ['number', 'capacity', 'beds']

class LevelSerializer(serializers.ModelSerializer):
    rooms = serializers.IntegerField(write_only=True)
    room_details = RoomSerializer(source='rooms', many=True, read_only=True)

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
        capacity = validated_data.pop('capacity')
        hostel = Hostel.objects.create(**validated_data)

        for level_data in levels_data:
            num_rooms = level_data.pop('rooms')
            level = Level.objects.create(hostel=hostel, **level_data)

            for room_number in range(1, num_rooms + 1):
                room = Room.objects.create(
                    level=level,
                    number=str(room_number).zfill(2),
                    capacity=capacity
                )

                for bed_number in range(1, capacity + 1):
                    Bed.objects.create(
                        room=room,
                        bed_number=str(bed_number).zfill(2),
                        status='available'
                    )

        return hostel

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['levels'] = sorted(
            representation['levels'],
            key=lambda x: x['number']
        )
        return representation
