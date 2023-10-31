from django.urls import path
from .views import AutoParkListView, AutoParkAddCarView, RetrieveUpdateDestroy
urlpatterns = [
    path('', AutoParkListView.as_view(), name='auto_park_list'),
    path('/<int:pk>', RetrieveUpdateDestroy.as_view(), name='auto_park_RUD'),
    path('/<int:pk>/car', AutoParkAddCarView.as_view(), name='auto_park_car_add'),
]

