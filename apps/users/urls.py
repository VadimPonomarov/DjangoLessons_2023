from rest_framework.urls import path
from .views import UserListCreateView, UserAddAvatarView, UserToggleIsActiveView, UserToggleIsStaffView
urlpatterns = [
    path('', UserListCreateView.as_view(), name='users_create_user'),
    path('/avatars', UserAddAvatarView.as_view(), name='users_add_avatar'),
    path('/is_active/<int:pk>', UserToggleIsActiveView.as_view(), name='user_toggle_is_active'),
    path('/is_staff/<int:pk>', UserToggleIsStaffView.as_view(), name='user_toggle_is_staff')
]
