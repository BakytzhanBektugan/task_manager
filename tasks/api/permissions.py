from rest_framework import permissions
from tasks.models import Task


class IsOwnerOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to get and edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Write/Read permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user