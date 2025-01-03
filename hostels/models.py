from django.db import models

class Hostel(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name

class Level(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='levels')
    number = models.IntegerField()

    def __str__(self):
        return f'{self.hostel.name} - Level {self.number}'

class Room(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='rooms')
    number = models.CharField(max_length=10)
    capacity = models.IntegerField()

    def __str__(self):
        return f'Room {self.number} (Level {self.level.number})'
