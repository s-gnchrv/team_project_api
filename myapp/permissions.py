from rest_framework import permissions


class IsTest(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name='test').exists()
