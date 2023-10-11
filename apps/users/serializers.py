from rest_framework import serializers
from .models import UserModel
from ..autoparks.serializers import AutoParkWithoutCarsSerializer


class UsersSerializer(serializers.ModelSerializer):
    auto_parks = AutoParkWithoutCarsSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = ('id', 'name', 'email', 'auto_parks')
        extra_args = {
            "created_at": {'write_only': True, 'required': False},
            "updated_at": {'write_only': True, 'required': False},
            'auto_parks': {"required": False}
        }
