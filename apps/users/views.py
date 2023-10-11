from rest_framework import status
from rest_framework.generics import ListCreateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import UserModel
from .serializers import UsersSerializer
from ..autoparks.serializers import AutoParkSerializer


class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UsersSerializer


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UsersSerializer


class UserAddReadAutoParkView(GenericAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UsersSerializer

    def post(self, *args, **kwargs):
        user = self.get_object()
        serializer = AutoParkSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

