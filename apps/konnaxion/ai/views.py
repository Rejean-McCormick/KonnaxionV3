from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.konnaxion.ai.models import AIResult
from apps/konnaxion.ai.serializers import AIResultSerializer
# Exemple : Importer la tâche d’analyse IA asynchrone
# from apps.konnaxion.ai.tasks import generate_ai_result

class AIResultViewSet(viewsets.ModelViewSet):
    """
    Endpoints pour les résultats générés par l’IA.
    Possède une action personnalisée pour déclencher le traitement IA sur un objet source.
    """
    queryset = AIResult.objects.all()
    serializer_class = AIResultSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'], url_path='generate', permission_classes=[permissions.IsAuthenticated])
    def generate(self, request):
        """
        Déclenche la génération d’un résultat IA pour un objet source.
        Expects 'source_model' et 'source_object_id' dans request.data.
        """
        source_model = request.data.get('source_model')
        source_object_id = request.data.get('source_object_id')
        if not source_model or not source_object_id:
            return Response({"error": "Les champs 'source_model' et 'source_object_id' sont requis."}, status=400)
        # Exemple : Appeler une tâche asynchrone
        # task = generate_ai_result.delay(source_model, source_object_id)
        return Response({
            "message": "Génération IA déclenchée",
            "source_model": source_model,
            "source_object_id": source_object_id
        })
