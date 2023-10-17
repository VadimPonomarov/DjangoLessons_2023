from django.urls import path, include

from apps.cars import urls as cars
from apps.autoparks import urls as auto_parks
from apps.auth import urls as auth
from apps.users import urls as users

urlpatterns = [
    path('cars', include(cars)),
    path('auto_parks', include(auto_parks)),
    path('auth', include(auth)),
    path('users', include(users)),
]
