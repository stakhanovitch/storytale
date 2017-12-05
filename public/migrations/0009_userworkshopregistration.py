# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-04 17:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('public', '0008_auto_20171204_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWorkshopRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('workshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public.Workshop')),
            ],
        ),
    ]