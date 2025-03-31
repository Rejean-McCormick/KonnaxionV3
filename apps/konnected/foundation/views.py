# apps/konnected/foundation/views.py

from rest_framework import viewsets, permissions
from konnected.foundation.models import KnowledgeUnit
from konnected.foundation.serializers import KnowledgeUnitSerializer

class KnowledgeUnitViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les Knowledge Units (contenu éducatif de base).
    """
    queryset = KnowledgeUnit.objects.all()
    serializer_class = KnowledgeUnitSerializer
    permission_classes = [permissions.IsAuthenticated]
