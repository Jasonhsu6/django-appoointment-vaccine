# Generated by Django 3.1.3 on 2020-11-18 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now=True, verbose_name='created at')),
                ('date', models.DateField(verbose_name='appointment date')),
                ('time', models.TimeField(verbose_name='appointment time')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('phone', models.CharField(max_length=14)),
                ('birthday', models.DateField(verbose_name='birthday')),
                ('description', models.TextField(verbose_name='description')),
            ],
            options={
                'verbose_name': 'Appointment',
                'verbose_name_plural': 'Appointments',
                'ordering': ['-date', 'time'],
            },
        ),
    ]
