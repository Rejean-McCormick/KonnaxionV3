# apps/keenkonnect/team_formation/views.py

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.keenkonnect.team_formation.models import TeamFormationRequest, TeamFormationCandidate
from apps.keenkonnect.team_formation.serializers import (
    TeamFormationRequestSerializer,
    TeamFormationCandidateSerializer
)
# Exemple : Importer une tâche asynchrone pour lancer la formation d'équipe basée sur l'IA
# from apps.keenkonnect.team_formation.tasks import trigger_team_formation

class TeamFormationRequestViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les demandes de formation d'équipe.
    """
    queryset = TeamFormationRequest.objects.all()
    serializer_class = TeamFormationRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def form_team(self, request, pk=None):
        """
        Action personnalisée pour déclencher le processus de formation d'équipe.
        """
        formation_request = self.get_object()
        # Exemple : déclencher la tâche asynchrone pour formation d'équipe
        # trigger_team_formation.delay(formation_request.id)
        return Response({"status": "Processus de formation déclenché", "request_id": formation_request.id})

class TeamFormationCandidateViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les candidats à la formation d'équipe.
    """
    queryset = TeamFormationCandidate.objects.all()
    serializer_class = TeamFormationCandidateSerializer
    permission_classes = [permissions.IsAuthenticated]
