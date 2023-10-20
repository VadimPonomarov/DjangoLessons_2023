from rest_framework import serializers
from .models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'model', 'year', 'price', 'image','auto_park_id')
        read_only_fields = ['image']
        extra_kwargs = {
            'created_at': {'write_only': True},
            'updated_at': {'write_only': True},
        }


class CarrAddImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['image']
