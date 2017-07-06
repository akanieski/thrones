# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import viewsets
from .serializers import LocationSerializer, LocationRatingSerializer
from .serializers import UserSerializer
from .models import Location, LocationRating
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAdminUser
from django.contrib.auth import get_user_model
from rest_framework import viewsets


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


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)

        return super(UserViewSet, self).get_permissions()
