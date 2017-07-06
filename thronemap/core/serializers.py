from rest_framework import serializers
from .models import Location, LocationRating
from django.contrib.auth.models import User
from rest_framework import serializers


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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'first_name', 'last_name', 'email', 'username')
        write_only_fields = ('password',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
