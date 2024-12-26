# Generated by Django 5.1.4 on 2024-12-25 16:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patienthistory', '0003_alter_medicineroutine_tags'),
        ('users', '0005_patientprofile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicineroutine',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.CreateModel(
            name='PatientBloodPressureRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('systolic', models.IntegerField(verbose_name='Systolic')),
                ('diastolic', models.IntegerField(verbose_name='Diastolic')),
                ('pulse_rate', models.IntegerField(verbose_name='Pulse Rate')),
                ('record_date', models.DateField(verbose_name='Record Date')),
                ('record_time', models.TimeField(verbose_name='Record Time')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.patientprofile', verbose_name='User')),
            ],
            options={
                'verbose_name': 'Patient Blood Pressure Record',
                'verbose_name_plural': 'Patient Blood Pressure Records',
                'ordering': ['record_date', 'record_time'],
            },
        ),
    ]