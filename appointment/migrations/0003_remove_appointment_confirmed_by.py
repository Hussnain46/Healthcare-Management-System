# Generated by Django 5.1.1 on 2024-09-24 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_appointment_confirmed_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='confirmed_by',
        ),
    ]