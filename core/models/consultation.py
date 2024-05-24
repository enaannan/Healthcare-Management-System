from django.db import models
from django.core.exceptions import ValidationError
import uuid
from core.models.user import User
class Consultation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(User, related_name='patient_consultations', on_delete=models.CASCADE)
    consultation_officer = models.ForeignKey(User, related_name='officer_consultations', on_delete=models.CASCADE)
    date = models.DateField()
    healthcare_provider = models.CharField(max_length=255)
    consultation_type = models.CharField(max_length=255)
    medical_condition = models.CharField(max_length=255)
    notes = models.TextField()

    def clean(self):
        if self.patient == self.consultation_officer:
            raise ValidationError('The patient and consultation officer cannot be the same person.')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['patient', 'consultation_officer'], name='unique_patient_officer')
        ]

    def save(self, *args, **kwargs):
        self.full_clean()  # This will call the clean method
        super().save(*args, **kwargs)
