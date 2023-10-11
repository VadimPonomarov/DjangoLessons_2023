from django.urls import path

from .views import UserListCreateView, UserRetrieveUpdateDestroyView, UserAddReadAutoParkView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='users_list_create'),
    path('/<int:pk>', UserRetrieveUpdateDestroyView.as_view(), name='users_RUD'),
]
