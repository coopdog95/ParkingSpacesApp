# Generated by Django 2.1.1 on 2018-11-19 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_parkingspace_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parkingspace',
            name='location',
        ),
    ]
