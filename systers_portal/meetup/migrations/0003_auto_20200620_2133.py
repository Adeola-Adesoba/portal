# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-06-20 21:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_squashed_0003_auto_20160207_1550'),
        ('meetup', '0002_meetup_meetup_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetuplocation',
            name='join_requests',
        ),
        migrations.RemoveField(
            model_name='meetuplocation',
            name='leader',
        ),
        migrations.RemoveField(
            model_name='meetuplocation',
            name='location',
        ),
        migrations.RemoveField(
            model_name='meetuplocation',
            name='members',
        ),
        migrations.RemoveField(
            model_name='meetuplocation',
            name='moderators',
        ),
        migrations.RemoveField(
            model_name='requestmeetuplocation',
            name='approved_by',
        ),
        migrations.RemoveField(
            model_name='requestmeetuplocation',
            name='location',
        ),
        migrations.RemoveField(
            model_name='requestmeetuplocation',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='meetup',
            options={'permissions': (('view_meetup_request', 'View Meetup Request'), ('approve_meetup_request', 'Approve Meetup Request'), ('reject_meetup_request', 'Reject Meetup Request'), ('add_meetups', 'Add Meetups'), ('delete_meetups', 'Delete Meetup'), ('change_meetups', 'Change Meetup'), ('add_meetup_rsvp', 'Add Meetup RSVP'), ('add_support_request', 'Add Support Request'), ('edit_support_request', 'Edit Support Request'), ('delete_support_request', 'Delete Support Request'), ('approve_support_request', 'Approve Support Request'), ('reject_support_request', 'Reject Support Request'), ('add_support_request_comment', 'Add Support Request Comment'))},
        ),
        migrations.AddField(
            model_name='meetup',
            name='leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='community_leader', to='users.SystersUser', verbose_name='Community leader'),
        ),
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
        migrations.DeleteModel(
            name='MeetupLocation',
        ),
        migrations.DeleteModel(
            name='RequestMeetupLocation',
        ),
    ]
