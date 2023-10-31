from django.conf.urls.static import static
from django.urls import path, include
from graphene_django.views import GraphQLView
from graphql_jwt.decorators import jwt_cookie
from rest_framework.permissions import AllowAny

from apps.cars import urls as cars
from apps.autoparks import urls as auto_parks
from apps.auth import urls as auth
from apps.users import urls as users
from apps.emails import urls as emails
from configs import settings
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
#     pass
schema_view = get_schema_view(
    openapi.Info(
        title='MyAPI',
        default_version='v1',
        description='Description',
        contact=openapi.Contact(email='my@gmail.com')
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('api/cars', include(cars)),
    path('api/auto_parks', include(auto_parks)),
    path('api/auth', include(auth)),
    path('api/users', include(users)),
    path('api/emails', include(emails)),
    path('api/graphql', jwt_cookie(csrf_exempt(GraphQLView.as_view(graphiql=True)))),
    path('api/doc', schema_view.with_ui('swagger', cache_timeout=0))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
