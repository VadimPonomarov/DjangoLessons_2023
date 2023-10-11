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
        fields = ('id', 'model', 'year', 'price', 'created_at', 'updated_at', 'auto_park_id')
        read_only_fields = ('created_at', 'updated_at')
        extra_kwargs = {
        }