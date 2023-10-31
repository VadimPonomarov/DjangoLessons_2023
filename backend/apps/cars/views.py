from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView, UpdateAPIView)

from core.permissions import ReadAuthenticated_CUDAdminPermission
from .filters import CarFilter
from .models import CarModel
from .serializers import CarSerializer, CarrAddImageSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.parsers import MultiPartParser


class CarView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    filterset_class = CarFilter
    permission_classes = [ReadAuthenticated_CUDAdminPermission]


class CarRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = [ReadAuthenticated_CUDAdminPermission]


class CarUpdateImageView(UpdateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarrAddImageSerializer
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser]
