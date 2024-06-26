from rest_framework import serializers

from core.models import User
from core.models.role import Role


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role_name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'date_of_birth', 'gender', 'contact_number', 'address',
                  'email', 'password', 'role_name']

    def get_role_name(self, obj):
        return obj.role.name if obj.role else None

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        role = validated_data.pop('role', None)
        user = User(**validated_data)
        user.set_password(password)

        if role:
            user.role = role

        user.save()

        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
