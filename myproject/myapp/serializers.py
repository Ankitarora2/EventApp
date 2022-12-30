from rest_framework import serializers
from .models import User, Event, Interest, Rating


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'location', 'date')


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ('user', 'event')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('user', 'event', 'rating')
