from rest_framework.permissions import IsAuthenticated


class IsSuperAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        if not super().haspemission(request, view):
            return False
        return request.user.is_superuser