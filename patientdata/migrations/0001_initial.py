# Generated by Django 5.1.4 on 2024-12-26 17:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_doctorprofile_patientprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PatientMedicineSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=50)),
                ('medicine_dosage', models.CharField(max_length=50)),
                ('medicine_frequency', models.IntegerField()),
                ('medicine_time', models.TimeField()),
                ('medicine_start_date', models.DateField(blank=True, null=True)),
                ('medicine_end_date', models.DateField(blank=True, null=True)),
                ('medicine_notes', models.TextField(blank=True, null=True)),
                ('medicine_days', models.ManyToManyField(related_name='schedules', to='patientdata.days')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.patientprofile')),
            ],
        ),
    ]
