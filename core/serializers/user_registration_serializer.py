from rest_framework import serializers

from core.models import User
from core.models.role import Role


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'date_of_birth', 'gender', 'contact_number', 'address',
                  'email', 'password','role_name']

    def get_role_name(self, obj):
        return obj.role.name
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        user.set_password(password)
        user.role = Role.objects.get(name=Role.OfficerRoles.PATIENT)
        user.save()
        return user

