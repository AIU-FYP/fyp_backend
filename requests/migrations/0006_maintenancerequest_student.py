# Generated by Django 5.1.4 on 2024-12-31 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0005_changeroomrequest_student_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenancerequest',
            name='student',
            field=models.CharField(default='', max_length=50),
        ),
    ]