# Generated by Django 5.1.4 on 2024-12-19 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('student_id', models.CharField(max_length=20, unique=True)),
                ('passport', models.ImageField(upload_to='passports/')),
                ('arrival_date', models.DateField()),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('religion', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
                ('major', models.CharField(max_length=100)),
                ('room_zone', models.CharField(max_length=100)),
            ],
        ),
    ]