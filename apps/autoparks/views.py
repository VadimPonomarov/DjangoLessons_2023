from rest_framework import status
from rest_framework.generics import ListCreateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import AutoParksModel
from .serializers import AutoParkSerializer
from ..cars.serializers import CarSerializer
from ..users.serializers import UsersSerializer


class AutoParkListView(ListCreateAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = AutoParkSerializer


class RetrieveUpdateDestroy(GenericAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = AutoParkSerializer


class AutoParkAddCarView(GenericAPIView):
    queryset = AutoParksModel.objects.all()

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        serializer = CarSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park_id=auto_park.id)
        auto_park_serializer = AutoParkSerializer(auto_park)
        return Response(auto_park_serializer.data, status=status.HTTP_201_CREATED)


class AutoParkAddUserView(GenericAPIView):
    queryset = AutoParksModel.objects.all()

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        serializer = UsersSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park=auto_park)
        return Response(serializer.data, status=status.HTTP_200_OK)
