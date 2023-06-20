from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class AddQuestion(permissions.BasePermission):
    """Class which allows user to update edit/update their own profile"""

    def has_permission(self, request, view):
        """Check if user has permission to perform the action"""
        if request.user.is_superuser and (request.method in permissions.SAFE_METHODS):
            return True
        if request.user.is_active and request.method == 'GET':
            return True
        raise PermissionDenied("You are not allowed to perform this action.")

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edit his own profile"""
        if request.user.is_superuser and (request.method in permissions.SAFE_METHODS):
            return True
        if request.user.is_active and request.method == 'GET':
            return True
        raise PermissionDenied("You are not allowed for this request")

class UpdateUseTemplate(permissions.BasePermission):
    """Class which allows user to update their own diary"""

    def has_permission(self, request, view):
        """Check if user has permission to perform the action"""
        if request.user.is_premium_user:
            return True
        raise PermissionDenied("You are not allowed to perform this action.")

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edit his own profile"""
        if request.user.is_superuser or request.user.is_premium_user:
            return True
        if request.method == 'GET':
            return True
        return False