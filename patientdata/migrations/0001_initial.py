# Generated by Django 5.1.4 on 2025-01-20 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='MedicineTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PatientMedicineSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=50)),
                ('medicine_dosage', models.CharField(max_length=50)),
                ('medicine_gap', models.IntegerField(blank=True, help_text='Gap between each dose in hours', null=True)),
                ('medicine_time', models.TimeField()),
                ('medicine_start_date', models.DateField(blank=True, null=True)),
                ('medicine_end_date', models.DateField(blank=True, null=True)),
                ('medicine_notes', models.TextField(blank=True, null=True)),
                ('medicine_days', models.ManyToManyField(related_name='schedules', to='patientdata.days')),
            ],
        ),
    ]
