# apps/keenkonnect/gap_analysis/views.py

from rest_framework import viewsets, permissions
from keenkonnect.gap_analysis.models import GapAnalysis
from keenkonnect.gap_analysis.serializers import GapAnalysisSerializer

class GapAnalysisViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les enregistrements d'analyse d'écart pour les projets.
    Permet de comparer le progrès prévu et réel et de stocker des recommandations.
    """
    queryset = GapAnalysis.objects.all()
    serializer_class = GapAnalysisSerializer
    permission_classes = [permissions.IsAuthenticated]
