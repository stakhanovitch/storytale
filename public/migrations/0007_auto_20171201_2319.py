# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-01 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0006_auto_20171201_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='subtitle',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
