import graphene
from graphene_django import DjangoObjectType

from apps.cars.models import CarModel


class CarType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    class Meta:
        model = CarModel
        fields = '__all__'
        filter_fields = {
            'id': ('exact', 'gt', 'contains'),
            'model': ('exact', 'contains'),
        }
        interfaces = (graphene.relay.Node,)
