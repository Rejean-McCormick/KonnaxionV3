# apps/ethikos/prioritization/views.py

from rest_framework import viewsets, permissions
from ethikos.prioritization.models import DebatePrioritization
from ethikos.prioritization.serializers import DebatePrioritizationSerializer

class DebatePrioritizationViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer le classement et le filtrage des débats.
    Les critères d'engagement et de crédibilité sont pris en compte dans le score.
    """
    queryset = DebatePrioritization.objects.all()
    serializer_class = DebatePrioritizationSerializer
    permission_classes = [permissions.IsAuthenticated]
