# Generated by Django 4.1.7 on 2023-05-02 10:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rounds',
            name='Participants',
        ),
        migrations.AlterField(
            model_name='rounds',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 2, 10, 24, 46, 602217, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='rounds',
            name='Participants',
            field=models.ManyToManyField(blank=True, to='event.registered'),
        ),
    ]
