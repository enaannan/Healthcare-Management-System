from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import User
from core.serializers.user_serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]