# apps/ethikos/knowledge_base/views.py

from rest_framework import viewsets, permissions
from ethikos.knowledge_base.models import DebateArchive
from ethikos.knowledge_base.serializers import DebateArchiveSerializer

class DebateArchiveViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer l'archivage des débats et des contenus de référence.
    """
    queryset = DebateArchive.objects.all()
    serializer_class = DebateArchiveSerializer
    permission_classes = [permissions.IsAuthenticated]
