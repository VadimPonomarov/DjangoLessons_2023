from django.conf.urls.static import static
from django.urls import path, include
from graphene_django.views import GraphQLView

from apps.cars import urls as cars
from apps.autoparks import urls as auto_parks
from apps.auth import urls as auth
from apps.users import urls as users
from apps.emails import urls as emails
from configs import settings

urlpatterns = [
    path('cars', include(cars)),
    path('auto_parks', include(auto_parks)),
    path('auth', include(auth)),
    path('users', include(users)),
    path('emails', include(emails) ),
    path("graphql", GraphQLView.as_view(graphiql=True)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
