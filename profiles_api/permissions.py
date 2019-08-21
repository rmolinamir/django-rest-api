from rest_framework.permissions import BasePermission, SAFE_METHODS


class UpdateOwnProfile(BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in SAFE_METHODS:
            return True

        """
        If it's not a safe method (put, patch, or delete), then return
        a comparison of the obj's id and the user's id who is requesting
        the edition of the object.
        """
        return obj.id == request.user.id
