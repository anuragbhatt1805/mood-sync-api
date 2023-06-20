from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class Slambook_Permission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        raise PermissionDenied("You are not athorized to perform this action")


class Answer_Permission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return True
        raise PermissionDenied("You are not athorized to perform this action")