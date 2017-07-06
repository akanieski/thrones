from rest_framework import serializers
from .models import Location, LocationRating


class LocationSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Location
        fields = (
            'id',
            'name',
            'latitude',
            'longitude',
            'is_accessible',
            'location_type',
            'is_family_friendly',
            'has_shower',
            'average_rating',
            # 'recent_comments'
        )


class LocationRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationRating
        fields = (
            'id',
            'rating',
            'note',
            'username',
            'posted_at',
            'location_id',
            'user_id'
        )
