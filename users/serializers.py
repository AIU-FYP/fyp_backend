from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name', 'position', 'staff_ID', 'phone', 'email', 'staff_type']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'profile']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        profile = instance.profile

        instance.username = validated_data.get('username', instance.username)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()

        profile.name = profile_data.get('name', profile.name)
        profile.position = profile_data.get('position', profile.position)
        profile.staff_ID = profile_data.get('staff_ID', profile.staff_ID)
        profile.phone = profile_data.get('phone', profile.phone)
        profile.email = profile_data.get('email', profile.email)
        profile.staff_type = profile_data.get('staff_type', profile.staff_type)
        profile.save()

        return instance


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['staff_type'] = self.user.profile.staff_type if hasattr(self.user, 'profile') else None
        data['user_id'] = self.user.id
        return data
