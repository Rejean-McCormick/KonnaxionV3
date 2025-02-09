from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.konnaxion.messaging.models import Conversation, Message
from apps.konnaxion.messaging.serializers import ConversationSerializer, MessageSerializer
# Exemple : Importer une tâche pour notifier en temps réel (WebSocket/Celery)
# from apps.konnaxion.messaging.tasks import notify_new_message

class ConversationViewSet(viewsets.ModelViewSet):
    """
    Endpoints pour la gestion des conversations.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

class MessageViewSet(viewsets.ModelViewSet):
    """
    Endpoints pour la gestion des messages.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def mark_as_read(self, request, pk=None):
        """
        Action personnalisée pour marquer un message comme lu.
        """
        message = self.get_object()
        message.is_read = True
        message.save()
        return Response({"status": "Message marqué comme lu"})

    def perform_create(self, serializer):
        message = serializer.save()
        # Exemple : Déclencher une tâche asynchrone pour notifier les destinataires en temps réel
        # notify_new_message.delay(message.id)
