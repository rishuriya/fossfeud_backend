# Generated by Django 4.2 on 2023-05-04 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_alter_gamerounds_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamerounds',
            name='deduction',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='games',
            name='award',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='games',
            name='deduction',
            field=models.IntegerField(default=0),
        ),
    ]