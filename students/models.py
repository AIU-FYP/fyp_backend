from django.db import models

from hostels.models import Room


class Student(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    passport = models.ImageField(upload_to='passports/')
    arrival_date = models.DateField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    religion = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    major = models.CharField(max_length=100)
    room_zone = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
