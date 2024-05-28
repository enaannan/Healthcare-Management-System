from django.urls import path, include
from rest_framework import routers

from core.views.current_user_view import CurrentUserView
from core.views.role_viewset import RoleViewSet
from core.views.user_viewset import UserViewSet
from core.views.consultation_viewset import ConsultationViewSet
from core.views.consultation_note_viewset import ConsultationNoteViewSet

router = routers.DefaultRouter()
router.register(r'roles', RoleViewSet)
router.register(r'users', UserViewSet)
router.register(r'consultations', ConsultationViewSet)
router.register(r'consultation-notes', ConsultationNoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('current-user/', CurrentUserView.as_view(), name='current-user'),
]
