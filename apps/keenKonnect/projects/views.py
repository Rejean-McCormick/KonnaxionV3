# apps/keenkonnect/projects/views.py

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from keenkonnect.projects.models import Project, Milestone, Task
from keenkonnect.projects.serializers import (
    ProjectSerializer,
    MilestoneSerializer,
    TaskSerializer
)

class ProjectViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les projets collaboratifs.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def change_status(self, request, pk=None):
        """
        Action personnalisée pour modifier le statut d'un projet.
        Par exemple : 'planning', 'in_progress', 'completed', etc.
        """
        project = self.get_object()
        new_status = request.data.get('status')
        if not new_status:
            return Response({'error': 'Le champ "status" est requis.'}, status=status.HTTP_400_BAD_REQUEST)
        project.status = new_status
        project.save()
        return Response(self.get_serializer(project).data)

class MilestoneViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les jalons (milestones) d'un projet.
    """
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer
    permission_classes = [permissions.IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les tâches d'un jalon de projet.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def mark_completed(self, request, pk=None):
        """
        Action personnalisée pour marquer une tâche comme complétée.
        """
        task = self.get_object()
        task.is_completed = True
        task.save()
        return Response(self.get_serializer(task).data)
