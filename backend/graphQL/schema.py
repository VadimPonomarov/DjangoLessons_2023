import graphene
import graphql_jwt
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.rest_framework.mutation import SerializerMutation
from graphql_auth.schema import MeQuery, UserQuery

from apps.autoparks.models import AutoParksModel
from apps.cars.filters import CarFilter
from apps.users.serializers import UserSerializer, UserSerializerBrief
from graphQL.types import CarType, AutoParkType
from graphql_jwt.refresh_token.signals import refresh_token_rotated

UserModel = get_user_model()


class Query(UserQuery, MeQuery, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    all_autoparks = graphene.List(AutoParkType)
    all_cars = DjangoFilterConnectionField(CarType, filterset_class=CarFilter)

    def resolve_all_autoparks(self, info):
        return AutoParksModel.objects.all()


class JwtMutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()

    @receiver(refresh_token_rotated)
    def revoke_refresh_token(sender, request, refresh_token, **kwargs):
        refresh_token.revoke(request)


class Mutation(JwtMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
