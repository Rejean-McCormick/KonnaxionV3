# apps/konnected/team/views.py

from rest_framework import viewsets, permissions
from apps.konnected.team.models import Team, TeamInvitation
from apps.konnected.team.serializers import TeamSerializer, TeamInvitationSerializer

class TeamViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer la création et la gestion des équipes éducatives.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]

class TeamInvitationViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les invitations à rejoindre une équipe.
    """
    queryset = TeamInvitation.objects.all()
    serializer_class = TeamInvitationSerializer
    permission_classes = [permissions.IsAuthenticated]
