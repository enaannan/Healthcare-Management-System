from rest_framework import serializers
from core.models.consultation import Consultation

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = '__all__'

    def create(self, validated_data):
        patient = validated_data.pop('patient')
        practitioner = validated_data.pop('practitioner')
        consultation = Consultation.objects.create(patient=patient, practitioner=practitioner, **validated_data)
        return consultation