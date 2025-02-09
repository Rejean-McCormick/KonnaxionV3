# apps/ethikos/debate_arena/views.py

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.ethikos.debate_arena.models import DebateSession, Argument, VoteRecord
from apps.ethikos.debate_arena.serializers import (
    DebateSessionSerializer,
    ArgumentSerializer,
    VoteRecordSerializer
)

class DebateSessionViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les sessions de débat en temps réel.
    """
    queryset = DebateSession.objects.all()
    serializer_class = DebateSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def end_session(self, request, pk=None):
        """
        Action pour clôturer une session de débat.
        Par exemple, en mettant à jour l'état et en enregistrant l'heure de fin.
        """
        session = self.get_object()
        session.is_active = False
        # Vous pouvez utiliser timezone.now() ou accepter une valeur dans request.data
        session.end_time = request.data.get('end_time')
        session.save()
        return Response(self.get_serializer(session).data)

class ArgumentViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les arguments dans une session de débat.
    """
    queryset = Argument.objects.all()
    serializer_class = ArgumentSerializer
    permission_classes = [permissions.IsAuthenticated]

class VoteRecordViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer l'enregistrement des votes sur les arguments.
    """
    queryset = VoteRecord.objects.all()
    serializer_class = VoteRecordSerializer
    permission_classes = [permissions.IsAuthenticated]
