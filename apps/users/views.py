from django.db.models import Q
from rest_framework.generics import ListCreateAPIView

from apps.users.models import UserModel
from apps.users.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated


class UserCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return UserModel.objects.filter(Q(id__gt=self.request.user.pk) | Q(id__lt=self.request.user.pk)).all()
