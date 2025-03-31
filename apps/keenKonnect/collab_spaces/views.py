# apps/keenkonnect/collab_spaces/views.py

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from keenkonnect.collab_spaces.models import CollabSpace, Document, ChatMessage
from keenkonnect.collab_spaces.serializers import (
    CollabSpaceSerializer,
    DocumentSerializer,
    ChatMessageSerializer
)
# Exemple : Importer une tâche asynchrone pour notifier les participants en temps réel
# from keenkonnect.collab_spaces.tasks import notify_new_chat_message

class CollabSpaceViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les espaces de collaboration.
    """
    queryset = CollabSpace.objects.all()
    serializer_class = CollabSpaceSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def add_participant(self, request, pk=None):
        """
        Action personnalisée pour ajouter un participant à un espace de collaboration.
        Attendu : un paramètre 'user_id' dans request.data.
        """
        collab_space = self.get_object()
        user_id = request.data.get('user_id')
        if not user_id:
            return Response({"error": "Le champ 'user_id' est requis."}, status=status.HTTP_400_BAD_REQUEST)
        # On suppose que l'ajout se fait via une méthode add_participant
        try:
            collab_space.participants.add(user_id)
            collab_space.save()
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(self.get_serializer(collab_space).data)

class DocumentViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les documents partagés dans un espace de collaboration.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

class ChatMessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les messages de chat dans un espace de collaboration.
    """
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def mark_as_read(self, request, pk=None):
        """
        Action pour marquer un message de chat comme lu.
        """
        message = self.get_object()
        message.is_read = True
        message.save()
        return Response(self.get_serializer(message).data)

    def perform_create(self, serializer):
        message = serializer.save()
        # Exemple : Déclencher une tâche asynchrone pour notifier les participants du nouvel envoi
        # notify_new_chat_message.delay(message.id)
