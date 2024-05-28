from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from core.models.consultation import Consultation
from core.serializers.consultation_serializer import ConsultationSerializer
from core.utils.custom_permission_class import IsOfficer, IsPatient


class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    permission_classes = [IsOfficer | IsPatient]
    search_fields = ['patient__first_name', 'patient__last_name','healthcare_provider','consultation_type','medical_condition']
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    def get_queryset(self):
        user = self.request.user
        if user.role.name == 'patient':
            return Consultation.objects.filter(patient=user)
        elif user.role.name in ['officer', 'superadmin']:
            return Consultation.objects.all()
        else:
            return Consultation.objects.none()