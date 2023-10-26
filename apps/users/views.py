from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import Token

from apps.users.serializers import UserSerializer, ProfileAvatarSerializer, UserSerializerBrief, \
    RecoveryEmailSerializer, RecoveryPasswordSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

from core.dataclasses import ProfileDataClass, UserDataClass
from core.permissions import SuperAdminPermission
from core.services.email import EmailService
from core.services.token import JWTService, ActivateToken, RecoveryToken
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserRecoveryEmailView(GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, *args, **kwargs):
        data = self.request.query_params
        serializer = RecoveryEmailSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(UserModel, **serializer.data)
        EmailService.recovery_email(user=user)
        return Response('Ok', status.HTTP_200_OK)


class UserAddAvatarView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileAvatarSerializer
    http_method_names = ('put',)

    def get_object(self):
        return UserModel.objects.get(pk=self.request.user.pk).profile

    def perform_update(self, serializer):
        profile: ProfileDataClass = self.get_object()
        profile.avatar.delete()
        super().perform_update(serializer)


class UserActivateView(GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, *args, **kwargs):
        token: Token = kwargs.get('token')
        user = JWTService.validate_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializerBrief(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserUpdatePasswordView(GenericAPIView):
    permission_classes = [AllowAny]
    queryset = UserModel.objects.all()

    def post(self, *args, **kwargs):
        token: Token = kwargs.get('token')
        user = JWTService.validate_token(token, RecoveryToken)
        password = self.request.data.get('password')
        serializer = RecoveryPasswordSerializer(data={'password': password})
        serializer.is_valid(raise_exception=True)
        user.set_password(password)
        user.save()
        return Response('Ok', status.HTTP_200_OK)


class UserToggleIsStaffView(UpdateAPIView):
    permission_classes = [SuperAdminPermission]

    def put(self, request, *args, **kwargs):
        user: UserDataClass = UserModel.objects.get(pk=kwargs.get('pk'))
        user.is_staff = True if not user.is_staff else False
        user.save()
        serializer = UserSerializerBrief(user)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs)
