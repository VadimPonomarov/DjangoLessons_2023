from rest_framework import serializers

from apps.autoparks.models import AutoParksModel
from apps.cars.serializers import CarSerializer


class AutoParkSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, required=False)

    class Meta:
        model = AutoParksModel
        fields = ('id', 'name', 'cars', 'created_at', 'updated_at')
        read_only_fields = ('cars',)


class AutoParkWithoutCarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoParksModel
        fields = ('id', 'name', 'created_at', 'updated_at')
