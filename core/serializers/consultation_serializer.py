from rest_framework import serializers
from core.models.consultation import Consultation
from core.models.user import User  # Import the User model if not already imported
from core.serializers.user_serializer import UserSerializer

class ConsultationSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    practitioner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Consultation
        fields = '__all__'

    def create(self, validated_data):
        patient = validated_data.pop('patient')
        practitioner = validated_data.pop('practitioner')
        consultation = Consultation.objects.create(patient=patient, practitioner=practitioner, **validated_data)
        return consultation

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['patient'] = UserSerializer(instance.patient).data
        representation['practitioner'] = UserSerializer(instance.practitioner).data
        return representation
