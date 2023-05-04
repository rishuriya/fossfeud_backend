# Generated by Django 4.1.7 on 2023-05-02 10:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_remove_rounds_participants_alter_rounds_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registered',
            name='Credits',
            field=models.IntegerField(default=300),
        ),
        migrations.AlterField(
            model_name='registered',
            name='Points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rounds',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 2, 10, 26, 13, 120328, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='rounds',
            name='Winner',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
