# Generated by Django 2.1.3 on 2018-11-14 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0003_auto_20181110_1435'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dictionary',
            old_name='url',
            new_name='src',
        ),
    ]