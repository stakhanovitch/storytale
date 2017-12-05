# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-05 15:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('public', '0009_userworkshopregistration'),
    ]

    operations = [
        migrations.AddField(
            model_name='userworkshopregistration',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterUniqueTogether(
            name='userworkshopregistration',
            unique_together=set([('user', 'workshop')]),
        ),
    ]