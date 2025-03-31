# apps/kreative/immersive/views.py

from rest_framework import viewsets, permissions
from kreative.immersive.models import ImmersiveExperience
from kreative.immersive.serializers import ImmersiveExperienceSerializer

class ImmersiveExperienceViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les expériences immersives (AR/VR).
    Ce module est minimal et peut être étendu ultérieurement.
    """
    queryset = ImmersiveExperience.objects.all()
    serializer_class = ImmersiveExperienceSerializer
    permission_classes = [permissions.IsAuthenticated]
