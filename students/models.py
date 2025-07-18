from django.db import models

from hostels.models import Hostel, Level, Room, Bed

class Student(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    STATUS_CHOICES = (
        ('active', 'Active'),
        ('foundation', 'Foundation'),
        ('inactive', 'Inactive'),
        ('graduated', 'Graduated'),
        ('terminated', 'Terminated'),
        ('internship', 'Internship')
    )

    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    passport = models.CharField(max_length=50, default='')
    arrival_date = models.DateField(null=True)
    phone = models.CharField(max_length=15 ,null=True)
    email = models.EmailField(unique=True ,null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    religion = models.CharField(max_length=50 ,null=True)
    nationality = models.CharField(max_length=50)
    major = models.CharField(max_length=100 ,null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    hostel = models.ForeignKey(Hostel, on_delete=models.SET_NULL, null=True, blank=True)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)
    bed = models.ForeignKey(Bed, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
