from rest_framework.permissions import IsAuthenticated

from core.models.role import Role


class IsSuperAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False
        return request.user.is_superuser

class IsOfficer(IsAuthenticated):
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False
        return request.user.role.name == Role.OfficerRoles.OFFICER