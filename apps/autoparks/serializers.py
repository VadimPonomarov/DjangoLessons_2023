from rest_framework import serializers

from apps.autoparks.models import AutoParksModel
from apps.cars.serializers import CarSerializer


class AutoParkSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = AutoParksModel
        fields = ('id', 'user', 'name', 'cars')
        read_only_fields = ('cars', 'user', 'created_at', 'updated_at',)


class AutoParkWithoutCarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoParksModel
        fields = ('id', 'user', 'name', 'created_at', 'updated_at')
        read_only_fields = ('user', 'created_at', 'updated_at',)
