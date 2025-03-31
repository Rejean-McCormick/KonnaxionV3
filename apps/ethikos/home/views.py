# apps/ethikos/home/views.py

from rest_framework import viewsets, permissions
from ethikos.home.models import DebateTopic, FeaturedDebate, PersonalizedRecommendation
from ethikos.home.serializers import (
    DebateTopicSerializer,
    FeaturedDebateSerializer,
    PersonalizedRecommendationSerializer
)

class DebateTopicViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les sujets de débat et catégories affichés sur le portail d'accueil.
    """
    queryset = DebateTopic.objects.all()
    serializer_class = DebateTopicSerializer
    permission_classes = [permissions.IsAuthenticated]

class FeaturedDebateViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les débats mis en avant sur le portail.
    """
    queryset = FeaturedDebate.objects.all()
    serializer_class = FeaturedDebateSerializer
    permission_classes = [permissions.IsAuthenticated]

class PersonalizedRecommendationViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les recommandations personnalisées affichées sur le portail.
    """
    queryset = PersonalizedRecommendation.objects.all()
    serializer_class = PersonalizedRecommendationSerializer
    permission_classes = [permissions.IsAuthenticated]
