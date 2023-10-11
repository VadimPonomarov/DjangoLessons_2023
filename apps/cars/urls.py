from django.urls import path

from apps.cars.views import CarView, CarRetrieveUpdateDeleteView

urlpatterns = [
    path('', CarView.as_view(), name='cars_list'),
    path('/<int:pk>', CarRetrieveUpdateDeleteView.as_view(), name='cars_retrieve_update_delete'),
]
