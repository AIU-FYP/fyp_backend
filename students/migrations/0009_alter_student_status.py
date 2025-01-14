# Generated by Django 5.1.4 on 2025-01-14 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_alter_student_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('graduated', 'Graduated'), ('terminated', 'Terminated')], default='active', max_length=20),
        ),
    ]
