# Generated by Django 2.1.3 on 2018-11-10 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0002_auto_20181110_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictionary',
            name='down',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dictionary',
            name='up',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
