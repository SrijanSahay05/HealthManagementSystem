# Generated by Django 5.1.4 on 2025-01-20 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointmentbooking', '0001_initial'),
        ('patientdata', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctoravailability',
            name='working_days',
            field=models.ManyToManyField(to='patientdata.days'),
        ),
    ]
