from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models.consultation_note import ConsultationNote
from core.serializers.ConsultationNoteSerializer import ConsultationNoteSerializer


class ConsultationNoteViewSet(viewsets.ModelViewSet):
    queryset = ConsultationNote.objects.all()
    serializer_class = ConsultationNoteSerializer
    permission_classes = [IsAuthenticated]