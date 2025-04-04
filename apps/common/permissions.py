from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission that only allows object owners to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Allow read-only permissions for any request
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        # Write permissions are only allowed to the owner.
        return getattr(obj, 'owner', None) == request.user
