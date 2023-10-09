from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .filters import car_filtered_queryset
from .models import CarModel
from .serializers import CarSerializer


class CarView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

    def get_queryset(self):
        return car_filtered_queryset(self.request.query_params)


class CarRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
