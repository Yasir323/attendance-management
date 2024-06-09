from rest_framework.permissions import BasePermission


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'manager'


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'staff'
