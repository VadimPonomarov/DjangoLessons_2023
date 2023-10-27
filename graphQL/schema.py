import graphene
from graphene_django_filter import AdvancedDjangoFilterConnectionField

from apps.autoparks.models import AutoParksModel
from graphQL.types import CarType, AutoParkType


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    all_autoparks = graphene.List(AutoParkType)
    all_cars = AdvancedDjangoFilterConnectionField(CarType)

    def resolve_all_autoparks(self, info):
        return AutoParksModel.objects.all()


schema = graphene.Schema(query=Query)
