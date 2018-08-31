# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.defaultfilters import slugify

from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100, default = None)
    address = models.CharField(max_length=100, default = None)
    post_code = models.IntegerField(default = None)
    town = models.CharField(max_length=100, default = None)

    def __str__(self):
        return self.name
