# apps/ethikos/stats/views.py

from rest_framework import viewsets, permissions
from ethikos.stats.models import DebateStatistic, DebateEventLog
from ethikos.stats.serializers import DebateStatisticSerializer, DebateEventLogSerializer

class DebateStatisticViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les statistiques des débats (ex. : nombre de votes, participants actifs).
    """
    queryset = DebateStatistic.objects.all()
    serializer_class = DebateStatisticSerializer
    permission_classes = [permissions.IsAuthenticated]

class DebateEventLogViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour consulter et enregistrer les logs d'événements des débats.
    """
    queryset = DebateEventLog.objects.all()
    serializer_class = DebateEventLogSerializer
    permission_classes = [permissions.IsAuthenticated]
