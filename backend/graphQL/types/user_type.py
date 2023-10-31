import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType

UserModel = get_user_model()


class UserType(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)

    class Meta:
        model = UserModel
        exclude = ['password']
        extra_kwargs = {
            "password": {"write_only": True}
        }
        interfaces = (graphene.relay.Node,)
