from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'email', 'is_superuser', 'is_staff', 'is_active']

        extra_kwargs = {
            'password': {'write_only': True},
            'user_permissions': {'write_only': True},
            'groups': {'write_only': True},
        }
