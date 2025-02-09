# apps/kreative/artworks/views.py

from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.kreative.artworks.models import Exhibition, Artwork
from apps.kreative.artworks.serializers import ExhibitionSerializer, ArtworkSerializer

class ExhibitionViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les expositions (création, modification, suppression et consultation).
    """
    queryset = Exhibition.objects.all()
    serializer_class = ExhibitionSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def activate(self, request, pk=None):
        """
        Action personnalisée pour activer/désactiver une exposition.
        Attendu : un booléen 'active' dans request.data.
        """
        exhibition = self.get_object()
        active = request.data.get('active')
        if active is None:
            return Response({"error": "Le champ 'active' est requis."}, status=400)
        exhibition.active = active
        exhibition.save()
        return Response(self.get_serializer(exhibition).data)

class ArtworkViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer le catalogue des œuvres.
    """
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def by_exhibition(self, request):
        """
        Retourne la liste des œuvres filtrées par l'exposition.
        Expects : un paramètre 'exhibition_id' dans les query params.
        """
        exhibition_id = request.query_params.get('exhibition_id')
        if exhibition_id:
            queryset = self.get_queryset().filter(exhibition_id=exhibition_id)
        else:
            queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
