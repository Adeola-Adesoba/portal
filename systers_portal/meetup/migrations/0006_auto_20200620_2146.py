# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-06-20 21:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0005_auto_20200620_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='meetup_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities_light.City', verbose_name='Meetup Location'),
        ),
        migrations.AlterField(
            model_name='requestmeetup',
            name='meetup_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities_light.City', verbose_name='Meetup Location'),
        ),
    ]
