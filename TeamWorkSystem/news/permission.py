from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return  obj.author == request.user 
# только автор может редактировать иные только чтение

class IsWriterOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return  obj.writer == request.user
# далее - объеденить классы - только (коментатор) может редактировать иные только чтение