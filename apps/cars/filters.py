from django_filters import rest_framework as filters

from .models import CarModel


class CarFilter(filters.FilterSet):
    year = filters.NumberFilter('year', 'exact')
    order = filters.OrderingFilter(
        fields=['id', 'year']
    )

    # class Meta:
    #     model = CarModel
    #     fields = ['id', 'year']