from django_filters import rest_framework as filters

from .models import CarModel


class CarFilter(filters.FilterSet):
    class Meta:
        model = CarModel
        fields = {
            'id': ['lte', 'gte', 'exact'],
            'year': ['lte', 'gte', 'exact'],
            'model': ['startswith', 'endswith', 'contains'],
        }

    order = filters.OrderingFilter(
        fields=(
            ('id', 'id ASC'),
            ('-id', 'id DESC'),
            ('year', 'year ASC'),
            ('-year', 'year DESC'),
            ('model', 'model ASC'),
            ('-model', 'model DESC'),
        )
    )
