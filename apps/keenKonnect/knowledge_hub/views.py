# apps/keenKonnect/knowledge_hub/views.py

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.keenKonnect.knowledge_hub.models import KnowledgeDocument, DocumentRevision
from apps.keenKonnect.knowledge_hub.serializers import (
    KnowledgeDocumentSerializer,
    DocumentRevisionSerializer
)
# Exemple : Importer une tâche asynchrone pour gérer la révision de document
# from apps.keenKonnect.knowledge_hub.tasks import trigger_document_revision

class KnowledgeDocumentViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les documents du Knowledge Hub.
    """
    queryset = KnowledgeDocument.objects.all()
    serializer_class = KnowledgeDocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def revise(self, request, pk=None):
        """
        Action personnalisée pour lancer une révision du document.
        """
        document = self.get_object()
        # Exemple : déclencher une tâche asynchrone de révision
        # trigger_document_revision.delay(document.id)
        return Response({"status": "Révision déclenchée", "document_id": document.id})

class DocumentRevisionViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les révisions des documents.
    """
    queryset = DocumentRevision.objects.all()
    serializer_class = DocumentRevisionSerializer
    permission_classes = [permissions.IsAuthenticated]
