# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-01 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0004_auto_20171201_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='subtitle',
            field=models.CharField(default=None, max_length=70, null=True),
        ),
    ]