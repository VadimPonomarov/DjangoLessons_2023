from rest_framework.urls import path
from .views import UserListCreateView, UserAddAvatarView, UserActivateView, UserToggleIsStaffView, UserRecoveryEmailView, UserUpdatePasswordView
urlpatterns = [
    path('', UserListCreateView.as_view(), name='users_create_user'),
    path('/avatars', UserAddAvatarView.as_view(), name='users_add_avatar'),
    path('/activate/<str:token>', UserActivateView.as_view(), name='users_user_active'),
    path('/recovery', UserRecoveryEmailView.as_view(), name='users_user_recovery_email'),
    path('/update_password/<str:token>', UserUpdatePasswordView.as_view(), name='users_user_update_password' ),
    path('/is_staff/<int:pk>', UserToggleIsStaffView.as_view(), name='user_toggle_is_staff')
]
