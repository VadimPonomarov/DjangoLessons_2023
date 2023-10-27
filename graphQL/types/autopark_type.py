from graphene_django import DjangoObjectType

from apps.cars.models import AutoParksModel


class AutoParkType(DjangoObjectType):
    class Meta:
        model = AutoParksModel
        fields = '__all__'
