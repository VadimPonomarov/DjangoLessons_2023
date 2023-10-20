from rest_framework import status
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.response import Response

from core.permissions import ReadAuthenticated_CUDAdminPermission
from .models import AutoParksModel
from .serializers import AutoParkSerializer
from ..cars.serializers import CarSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class AutoParkListView(ListCreateAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = AutoParkSerializer
    permission_classes = [ReadAuthenticated_CUDAdminPermission]


class RetrieveUpdateDestroy(GenericAPIView):
    queryset = AutoParksModel.objects.all()
    serializer_class = AutoParkSerializer
    permission_classes = [ReadAuthenticated_CUDAdminPermission]


class AutoParkAddCarView(GenericAPIView):
    queryset = AutoParksModel.objects.all()
    permission_classes = [ReadAuthenticated_CUDAdminPermission]

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        serializer = CarSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park_id=auto_park.id)
        auto_park_serializer = AutoParkSerializer(auto_park)
        return Response(auto_park_serializer.data, status=status.HTTP_201_CREATED)
