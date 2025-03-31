# apps/ethikos/resolution/views.py

from rest_framework import viewsets, permissions
from ethikos.resolution.models import DebateResolution
from ethikos.resolution.serializers import DebateResolutionSerializer

class DebateResolutionViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer la documentation des résolutions de débats.
    Chaque résolution inclut l'audit trail complet des décisions.
    """
    queryset = DebateResolution.objects.all()
    serializer_class = DebateResolutionSerializer
    permission_classes = [permissions.IsAuthenticated]
