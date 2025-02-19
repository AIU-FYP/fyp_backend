from django.db import models
from students.models import Student


class MaintenanceRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('rejected', 'Rejected'),
    )

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    student_id = models.CharField(max_length=20, default='')
    student = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=15, default='')
    email = models.EmailField(default='')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')
    nationality = models.CharField(max_length=50, default='')
    room_number = models.CharField(max_length=10)
    issue = models.CharField(max_length=255)
    occurrence = models.CharField(max_length=255)
    evidence_photo = models.FileField(upload_to='maintenance_evidence/', default='null')
    explanation = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f'Request by {self.student_id}'


class ChangeRoomRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    student_id = models.CharField(max_length=20, default='')
    student = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=15, default='')
    email = models.EmailField(default='')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')
    nationality = models.CharField(max_length=50, default='')
    room_number = models.CharField(max_length=10)
    supporting_doc = models.FileField(upload_to='change_room_docs/')
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES , default = 'pending')

    def __str__(self):
        return f'Change Room Request by {self.student_id}'
