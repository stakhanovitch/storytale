# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.defaultfilters import slugify

from django.db import models
from django.utils import timezone
from django.urls import reverse
from public.models.location import Location

class Workshop(models.Model):

    image = models.ImageField(max_length=500, upload_to='workshops', null = True, blank = True)
    title = models.CharField(max_length=100, default = None)
    description =  models.TextField(null = True, blank = True)
    date_created = models.DateTimeField(default=timezone.now)
    start_time = models.DateTimeField(null = True, blank = True)
    end_time = models.DateTimeField(null = True, blank = True)
    max_attendance = models.IntegerField(null = True, blank = True)
    location = models.ForeignKey(Location)
    signup_url = models.URLField( blank = True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null = True, blank = True)
    slug = models.SlugField(max_length=255, blank=True,)

    def __str__(self):
        return self.title

    def printed_price(self):
        return str(self.price) + " €"


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Workshop, self).save(*args, **kwargs)

    def duration (self, *args, **kwargs):
        duration =  self.end_time - self.start_time
        return duration

    def get_absolute_url(self):
        return reverse('workshopregistration', args=[self.slug])

    def __unicode__(self):
        return u'%s'%(self.description)

    def __unicode__(self):
        return u'%s'%(self.title)
