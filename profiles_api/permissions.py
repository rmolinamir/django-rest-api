from rest_framework.permissions import BasePermission, SAFE_METHODS


class UpdateOwnProfile(BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        """get requests:"""
        if request.method in SAFE_METHODS:
            return True

        """
        If it's not a safe method (put, patch, or delete), then return
        a comparison of the obj's id and the user's id who is requesting
        the edition of the object.
        """
        return obj.id == request.user.id


class UpdateOwnStatus(BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check if the user is trying to update their own status"""
        """get requests:"""
        if request.method in SAFE_METHODS:
            return True

        """
        Check if the user_profile property in the obj that is being updated
        is the same as the user in the request object (so long as the user is
        authenticated, it will be in the request object).
        """
        return obj.user_profile.id == request.user.id
