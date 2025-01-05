# Generated by Django 5.1.4 on 2025-01-05 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostels', '0003_remove_room_status_bed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bed',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('occupiedd', 'Occupied'), ('under_maintenance', 'Under Maintenance')], default='available', max_length=20),
        ),
    ]