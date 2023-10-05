from django.urls import path

from apps.cars.views import CarView, CarRetrieveUpdateDeleteView

urlpatterns = [
    path('cars', CarView.as_view()),
    path('cars/<int:pk>', CarRetrieveUpdateDeleteView.as_view()),
]
