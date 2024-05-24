from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models.consultation import Consultation
from core.serializers.consultation_serializer import ConsultationSerializer


class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    permission_classes = [IsAuthenticated]