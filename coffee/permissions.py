from rest_framework import permissions

class IsMakerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if obj.maker is None:
            return True

        return obj.maker == request.user