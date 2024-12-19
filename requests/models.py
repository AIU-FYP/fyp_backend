from django.db import models
from students.models import Student

class MaintenanceRequest(models.Model):
    STATUS_CHOICES = (
        ('ppk_done', 'PPK Done'),
        ('rejected', 'Rejected'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='maintenance_requests')
    room_number = models.CharField(max_length=10)
    issue = models.CharField(max_length=255)
    occurrence = models.CharField(max_length=255)
    evidence_photo = models.ImageField(upload_to='maintenance_evidence/')
    explanation = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f'Request by {self.student.name}'

class ChangeRoomRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='change_room_requests')
    room_number = models.CharField(max_length=10)
    supporting_doc = models.FileField(upload_to='change_room_docs/')
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f'Change Room Request by {self.student.name}'
