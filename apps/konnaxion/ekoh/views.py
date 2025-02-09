from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.konnaxion.ekoh.models import ExpertiseTag, ReputationProfile, ReputationEvent, WeightedVote
from apps.konnaxion.ekoh.serializers import (
    ExpertiseTagSerializer,
    ReputationProfileSerializer,
    ReputationEventSerializer,
    WeightedVoteSerializer
)
# Exemple : Importer une tâche pour recalculer la réputation
# from apps.konnaxion.ekoh.tasks import recalculate_reputation

class ExpertiseTagViewSet(viewsets.ModelViewSet):
    """
    Endpoints pour gérer les tags d'expertise.
    """
    queryset = ExpertiseTag.objects.all()
    serializer_class = ExpertiseTagSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReputationProfileViewSet(viewsets.ModelViewSet):
    """
    Endpoints pour consulter et mettre à jour le profil de réputation des utilisateurs.
    """
    queryset = ReputationProfile.objects.all()
    serializer_class = ReputationProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReputationEventViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Endpoints en lecture seule pour consulter les événements impactant la réputation.
    """
    queryset = ReputationEvent.objects.all()
    serializer_class = ReputationEventSerializer
    permission_classes = [permissions.IsAuthenticated]

class WeightedVoteViewSet(viewsets.ModelViewSet):
    """
    Endpoints pour la gestion des votes pondérés.
    À la création d'un vote, un recalcul asynchrone de la réputation peut être déclenché.
    """
    queryset = WeightedVote.objects.all()
    serializer_class = WeightedVoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        vote = serializer.save()
        # Exemple : Déclencher la tâche de recalcul de réputation
        # recalculate_reputation.delay(vote.user.id, vote.target_id, vote.vote_value)
