from django.db import models
from django.core.exceptions import ValidationError
import uuid

class Consultation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey('User', related_name='patient_consultations', on_delete=models.CASCADE)
    practitioner = models.ForeignKey('User', related_name='officer_consultations', on_delete=models.CASCADE)
    date = models.DateField()
    healthcare_provider = models.CharField(max_length=255)
    consultation_type = models.CharField(max_length=255)
    medical_condition = models.CharField(max_length=255)

    def clean(self):
        if self.patient == self.practitioner:
            raise ValidationError('The patient and practitioner cannot be the same person.')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['patient', 'practitioner'], name='unique_patient_practitioner')
        ]
