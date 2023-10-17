from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.auth.serializers import MeSerializer


class MeView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MeSerializer

    def get(self, *args, **kwargs):
        user = self.request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
