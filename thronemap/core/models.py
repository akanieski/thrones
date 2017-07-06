# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

LOCATION_TYPE = (
    (1, 'Restaurant'),
    (2, 'Office'),
    (3, 'Public Restroom'),
    (4, 'Cafe'),
    (5, 'School'),
    (6, 'Library'),
    (7, 'Retail'),
    (8, 'Other')
)


class Location(models.Model):
    name = models.CharField(max_length=255, blank=False)
    latitude = models.FloatField(blank=False, db_index=True)
    longitude = models.FloatField(blank=False, db_index=True)
    is_accessible = models.BooleanField(blank=False, default=False)
    location_type = models.SmallIntegerField(blank=False, 
                                             choices=LOCATION_TYPE)
    is_family_friendly = models.BooleanField(blank=False, default=False)
    has_shower = models.BooleanField(blank=False, default=False)

    @property
    def average_rating(self):
        return self.locationrating_set.aggregate(
            average=Avg('rating')
        )['average']

    @property
    def recent_comments(self):
        return [{
            'id': r.pk,
            'posted_at': r.posted_at,
            'note': r.note,
            'username': r.username,
            'rating': r.rating
        } for r in self.locationrating_set.all()[:5]]


class LocationRating(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(blank=False, db_index=True, default=0)
    user = models.ForeignKey(User, on_delete=None, null=True)
    posted_at = models.DateTimeField(blank=False, auto_now=True)
    note = models.TextField(blank=True, default='', null=False)

    @property
    def username(self):
        return self.user.username
