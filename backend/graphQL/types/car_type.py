import graphene
from graphene_django import DjangoObjectType

from apps.cars.models import CarModel


class CarType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    class Meta:
        model = CarModel
        fields = '__all__'
        interfaces = (graphene.relay.Node,)

