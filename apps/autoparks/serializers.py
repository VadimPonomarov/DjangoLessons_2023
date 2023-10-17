from rest_framework import serializers

from apps.autoparks.models import AutoParksModel
from apps.cars.serializers import CarSerializer


class AutoParkSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, required=False)

    class Meta:
        model = AutoParksModel
        fields = ('id', 'name', 'cars')
        read_only_fields = ('cars',)
        extra_kwargs = {
            'created_at': {'write_only': True},
            'updated_at': {'write_only': True},
        }


class AutoParkWithoutCarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoParksModel
        fields = ('id', 'name', 'created_at', 'updated_at')
