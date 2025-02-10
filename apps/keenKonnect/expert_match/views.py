# apps/keenkonnect/expert_match/views.py

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.keenkonnect.expert_match.models import ExpertMatchRequest, CandidateProfile, MatchScore
from apps.keenkonnect.expert_match.serializers import (
    ExpertMatchRequestSerializer,
    CandidateProfileSerializer,
    MatchScoreSerializer
)
# Exemple : Importer une tâche asynchrone pour lancer l'algorithme de matching
# from apps.keenkonnect.expert_match.tasks import trigger_expert_matching

class ExpertMatchRequestViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les demandes de mise en relation avec des experts.
    """
    queryset = ExpertMatchRequest.objects.all()
    serializer_class = ExpertMatchRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def trigger_match(self, request, pk=None):
        """
        Action personnalisée pour déclencher le processus de matching.
        (Ici, vous pouvez appeler une tâche asynchrone par exemple.)
        """
        match_request = self.get_object()
        # Exemple : déclencher la tâche asynchrone
        # trigger_expert_matching.delay(match_request.id)
        return Response({"status": "Matching déclenché", "match_request_id": match_request.id})

class CandidateProfileViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les profils candidats pour le matching.
    """
    queryset = CandidateProfile.objects.all()
    serializer_class = CandidateProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class MatchScoreViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour consulter et enregistrer les scores de compatibilité.
    """
    queryset = MatchScore.objects.all()
    serializer_class = MatchScoreSerializer
    permission_classes = [permissions.IsAuthenticated]
