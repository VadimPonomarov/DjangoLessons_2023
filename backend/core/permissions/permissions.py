from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class SuperAdminPermission(BasePermission):
    def has_permission(self, request: Request, view):
        return bool(request.user and request.user.is_staff and request.user.is_superuser and request.user.is_active)


class ReadAuthenticated_CUDAdminPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return bool(request.user and request.user.is_active)
        return bool(request.user and request.user.is_staff and request.user.is_active)


class IsStaffOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff and request.user.is_active and not request.user.is_superuser)
