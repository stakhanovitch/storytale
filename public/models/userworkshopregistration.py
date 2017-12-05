# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.defaultfilters import slugify

from django.contrib.auth.models import User
from public.models.workshop import Workshop

from django.db import models
from django.utils import timezone


class UserWorkshopRegistration(models.Model):
    user = models.ForeignKey(User)
    workshop = models.ForeignKey(Workshop)
    date_created = models.DateTimeField(default=timezone.now)
    class Meta:
        unique_together = ("user","workshop")
