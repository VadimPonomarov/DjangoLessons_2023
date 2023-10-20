from rest_framework import status
from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework.response import Response

from apps.users.models import UserModel
from apps.users.serializers import UserSerializer, ProfileAvatarSerializer, UserSerializerBrief
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from core.dataclasses import ProfileDataClass, UserDataClass


class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


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


class UserToggleIsActiveView(UpdateAPIView):
    permission_classes = [IsAdminUser]
    def put(self, request, *args, **kwargs):
        user: UserDataClass = UserModel.objects.get(pk=kwargs.get('pk'))
        if user.is_superuser:
            raise PermissionError('Not permission')
        user.is_active = True if not user.is_active else False
        user.save()
        serializer = UserSerializerBrief(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserToggleIsStaffView(UpdateAPIView):
    def put(self, request, *args, **kwargs):
        user: UserDataClass = UserModel.objects.get(pk=kwargs.get('pk'))
        if user.is_superuser:
            return Response('!!! Forbidden', status.HTTP_403_FORBIDDEN)
        user.is_staff = True if not user.is_staff else False
        user.save()
        serializer = UserSerializerBrief(user)
        return Response(serializer.data, status.HTTP_200_OK)
