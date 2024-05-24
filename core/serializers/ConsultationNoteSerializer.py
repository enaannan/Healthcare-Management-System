from rest_framework import serializers

from core.models.consultation_note import ConsultationNote


class ConsultationNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultationNote
        fields = '__all__'