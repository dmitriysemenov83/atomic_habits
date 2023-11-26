from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Разрешить чтение и запись только владельцу привычки
        return obj.user == request.user


class CanViewPublicHabits(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Разрешить просмотр только владельцу привычки или если привычка публичная
        return obj.user == request.user or obj.is_public

