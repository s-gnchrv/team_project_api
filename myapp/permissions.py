from rest_framework import permissions


class IsContactor(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name='contactor').exists()


class IsRepresentative(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name='representative').exists()


class IsRepresentativeOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.groups.filter(name='representative').exists()


class IsRepresentativeAndCreator(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.groups.filter(name='representative').exists() and obj.creator == request.user


class IsCreatorOrExecutor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user or obj.executor == request.user


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
