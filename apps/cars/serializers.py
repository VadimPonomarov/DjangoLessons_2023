from rest_framework import serializers
from .models import CarModel


# class CarSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     model = serializers.CharField(max_length=25)
#     year = serializers.IntegerField()
#     seats = serializers.IntegerField(write_only=True)
#     type = serializers.CharField(write_only=True, max_length=25)
#     engine_v = serializers.FloatField(write_only=True)
#
#     def create(self, validated_data):
#         car = CarModel.objects.create(**validated_data)
#         return car
#
#     def update(self, instance, validated_data):
#         for k, v in validated_data.items():
#             setattr(instance, k, v)
#         instance.save()
#         return instance

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'model', 'year', 'price', 'auto_park_id')
        extra_kwargs = {
            'created_at': {'write_only': True},
            'updated_at': {'write_only': True},
        }
