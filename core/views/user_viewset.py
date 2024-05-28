from rest_framework import viewsets
from rest_framework import filters

from core.models import User
from core.serializers.user_serializer import UserSerializer
from core.utils.custom_permission_class import IsSuperAdmin, IsOfficer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOfficer | IsSuperAdmin]
    search_fields = ['first_name', 'last_name', 'email', 'role__name']
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]