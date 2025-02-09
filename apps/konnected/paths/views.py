# apps/konnected/paths/views.py

from rest_framework import viewsets, permissions
from apps.konnected.paths.models import LearningPath, PathStep
from apps.konnected.paths.serializers import LearningPathSerializer, PathStepSerializer

class LearningPathViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer la création et la modification des parcours d'apprentissage.
    """
    queryset = LearningPath.objects.all()
    serializer_class = LearningPathSerializer
    permission_classes = [permissions.IsAuthenticated]

class PathStepViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les étapes individuelles d'un parcours d'apprentissage.
    """
    queryset = PathStep.objects.all()
    serializer_class = PathStepSerializer
    permission_classes = [permissions.IsAuthenticated]
