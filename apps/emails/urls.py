from django.urls import path
from .views import TestEmailView

urlpatterns = [
    path('/test', TestEmailView.as_view())
]
