# Generated by Django 5.1.4 on 2025-01-05 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostels', '0002_room_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='status',
        ),
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('available', 'Available'), ('occupied', 'Occupied'), ('under_maintenance', 'Under Maintenance')], default='available', max_length=20)),
                ('bed_number', models.CharField(default='', max_length=10)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beds', to='hostels.room')),
            ],
        ),
    ]