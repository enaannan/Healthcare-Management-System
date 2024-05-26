from django.db import models
import uuid

class Role(models.Model):
    class OfficerRoles(models.TextChoices):
        PATIENT = 'patient', 'Patient'
        DOCTOR = 'doctor', 'Doctor'
        NURSE = 'nurse', 'Nurse'
        PHARMACIST = 'pharmacist', 'Pharmacist'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, choices=OfficerRoles.choices, default=OfficerRoles.PATIENT,unique=True)


    def __str__(self):
        return self.name

