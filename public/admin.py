# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from public.models import Workshop, Location, UserWorkshopRegistration

admin.site.register(Workshop)
admin.site.register(Location)
admin.site.register(UserWorkshopRegistration)
# Register your models here.
