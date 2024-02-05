# Generated by Django 5.0.1 on 2024-02-04 17:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flight', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile_no', models.CharField(max_length=12)),
                ('class_type', models.CharField(choices=[('Business', 'Business'), ('Economy', 'Economy')], max_length=20)),
                ('is_booked', models.BooleanField(default=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('flight_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.flight')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
