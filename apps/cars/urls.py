from django.urls import path

from apps.cars.views import CarView, CarRetrieveUpdateDeleteView, CarUpdateImageView

urlpatterns = [
    path('', CarView.as_view(), name='cars_list'),
    path('/<int:pk>', CarRetrieveUpdateDeleteView.as_view(), name='cars_retrieve_update_delete'),
    path('/image/<int:pk>', CarUpdateImageView.as_view(), name='cars_update_image')
]
