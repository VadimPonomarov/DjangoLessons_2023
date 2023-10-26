import re
from django.core import validators as V
from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.users.models import UserModel, ProfileModel
from django.db.transaction import atomic

from apps.users.regex import UserRegEx
from core.dataclasses import UserDataClass, ProfileDataClass
from core.services.email import EmailService

UserModel = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'surname', 'age', 'avatar', 'created_at', 'updated_at')

    def validate_age(self, value: int):
        if value < 18 or value > 40:
            raise serializers.ValidationError('Age should be Integer between 18 and 40')
        return value


class ProfileAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('avatar',)
        extra_kwargs = {
            'avatar': {
                'required': True
            }
        }


class UserSerializerBrief(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'is_staff', 'is_superuser', 'is_active', 'last_login', 'created_at',
            'updated_at'
        )
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_staff', 'is_superuser', 'is_active', 'last_login', 'created_at',
            'updated_at', 'profile'
        )
        read_only_fields = (
            'id', 'is_staff', 'is_superuser', 'is_active', 'last_login', 'created_at', 'updated_at')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    @atomic
    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')
        profile = ProfileModel.objects.create(**profile)
        user = UserModel.objects.create_user(profile=profile, **validated_data)
        EmailService.register_email(user)
        return user


class RecoveryEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class RecoveryPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['password']
