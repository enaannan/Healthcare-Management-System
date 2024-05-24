from django.db import models
import uuid

from . import User
from .consultation import Consultation

class ConsultationNote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    consultation = models.ForeignKey(Consultation, related_name='notes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note_type = models.CharField(max_length=255)
    note_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
