from rest_framework import generics

from core.models import User
from core.serializers.user_registration_serializer import UserRegistrationSerializer
from rest_framework.permissions import AllowAny


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]