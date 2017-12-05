# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.defaultfilters import slugify

from django.db import models
from django.utils import timezone
from django.urls import reverse

class Workshop(models.Model):

    title = models.CharField(max_length=70, default = None)
    subtitle = models.CharField(max_length=70, null = True, blank = True)
    description =  models.TextField(null = True, blank = True)
    date_created = models.DateTimeField(default=timezone.now)
    start_time = models.DateTimeField(null = True, blank = True)
    end_time = models.DateTimeField(null = True, blank = True)
    max_attendance = models.IntegerField(null = True, blank = True)
    location = models.TextField()
    slug = models.SlugField(blank=True,)

    def __str__(self):
        return self.title

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
    def __unicode__(self):
        return u'%s'%(self.subtitle)
