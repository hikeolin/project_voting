from rest_framework import permissions


class IsAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, object):
        return request.user.active and \
            (request.user.admin and request.user.is_admin) 

class IsSuperUser(permissions.BasePermission):

    def has_object_permission(self, request, view, object):
        return request.user.active and request.user.is_superuser
        
class IsStaff(permissions.BasePermission):

    def has_object_permission(self, request, view, object):
        return request.user.active and request.user.staff