# Generated by Django 4.2 on 2023-05-02 11:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_rounds_status_alter_rounds_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rounds',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 2, 11, 19, 47, 444359, tzinfo=datetime.timezone.utc)),
        ),
    ]
