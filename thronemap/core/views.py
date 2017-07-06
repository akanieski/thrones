# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import generics
from .serializers import LocationSerializer, LocationRatingSerializer
from .models import Location, LocationRating


class LocationsView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Location."""
        serializer.save()


class LocationDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationRatingsView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = LocationRating.objects.all()
    serializer_class = LocationRatingSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Location."""
        serializer.save(
            location_id=self.kwargs['pk'],
            user_id=self.request.user.id
        )

    def get_queryset(self):
        """
        This view should return a list of all the ratings for
        the location as determined by the location_id portion of the URL.
        """
        location_id = self.kwargs['pk']
        return LocationRating.objects.filter(location_id=location_id)


class LocationRatingDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = LocationRating.objects.all()
    serializer_class = LocationRatingSerializer
