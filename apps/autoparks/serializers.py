from rest_framework import serializers

from apps.autoparks.models import AutoParksModel
from apps.cars.serializers import CarSerializer


class AutoParkSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = AutoParksModel
        fields = ('id', 'name', 'created_at', 'updated_at', 'cars', 'user')
        read_only_fields = ('cars', 'user')


class AutoParkWithoutCarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoParksModel
        fields = ('id', 'name', 'created_at', 'updated_at')
