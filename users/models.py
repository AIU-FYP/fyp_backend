from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Profile(models.Model):
    USER_TYPES = (
        ('admin', 'Admin'),
        ('super_admin', 'Super Admin'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    staff_ID = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    staff_type = models.CharField(max_length=20, choices=USER_TYPES)

    def __str__(self):
        return self.name
