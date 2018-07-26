# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-07-03 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buses', '0002_location_bus_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busparameter',
            name='distance',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='busparameter',
            name='fuel',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='busparameter',
            name='speed',
            field=models.FloatField(),
        ),
    ]
