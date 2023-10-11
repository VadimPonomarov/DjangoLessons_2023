from django.urls import path
from .views import AutoParkListView, AutoParkAddCarView, RetrieveUpdateDestroy, AutoParkAddUserView
urlpatterns = [
    path('', AutoParkListView.as_view(), name='auto_park_list'),
    path('/<int:pk>', RetrieveUpdateDestroy.as_view(), name='auto_park_RUD'),
    path('/<int:pk>/car', AutoParkAddCarView.as_view(), name='auto_park_car_add'),
    path('/<int:pk>/user', AutoParkAddUserView.as_view(), name='auto_park_user_add'),
]

