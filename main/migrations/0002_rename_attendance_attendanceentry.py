# Generated by Django 4.2.13 on 2024-06-20 22:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Attendance',
            new_name='AttendanceEntry',
        ),
    ]
