from rest_framework import permissions


class AuthorRightsPermission(permissions.BasePermission):
    """
    Allows User to add or edit only his own post, preventing other users to do it
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Checking, if request user is the same with logged in user
        return obj == request.user


class AuthorRightsPermissionPost(permissions.BasePermission):
    """
    Allows User to add or edit only his own post, preventing other users to do it
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Checking, if id of post author is the same with id of currently logged in user
        return obj.author.id == request.user.id


class CommentAuthorRightsPermission(permissions.BasePermission):
    """
    Allows User to add or edit only his own comment, preventing other users to do it
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Checking, if id of post author is the same with id of currently logged in user
        return obj.comment_author.id == request.user.id
