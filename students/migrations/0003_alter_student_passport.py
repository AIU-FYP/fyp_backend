# Generated by Django 5.1.4 on 2024-12-29 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='passport',
            field=models.CharField(default='', max_length=50),
        ),
    ]