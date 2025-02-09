# apps/kreative/marketplace/views.py

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.kreative.marketplace.models import ArtistProfile, Commission, MarketplaceListing
from apps.kreative.marketplace.serializers import (
    ArtistProfileSerializer,
    CommissionSerializer,
    MarketplaceListingSerializer
)

class ArtistProfileViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les profils d'artistes.
    Permet aux artistes de gérer leur profil et leur portfolio.
    """
    queryset = ArtistProfile.objects.all()
    serializer_class = ArtistProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommissionViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les commissions artistiques.
    Permet de créer, mettre à jour et suivre les demandes de commissions.
    """
    queryset = Commission.objects.all()
    serializer_class = CommissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def update_status(self, request, pk=None):
        """
        Action personnalisée pour mettre à jour le statut d'une commission.
        Par exemple, passer de 'requested' à 'in_progress' ou 'completed'.
        """
        commission = self.get_object()
        new_status = request.data.get('status')
        if not new_status:
            return Response({"error": "Le champ 'status' est requis."},
                            status=status.HTTP_400_BAD_REQUEST)
        commission.status = new_status
        commission.save()
        return Response(self.get_serializer(commission).data)

class MarketplaceListingViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les annonces du marketplace.
    Permet de créer, mettre à jour et supprimer des annonces d'œuvres ou de commissions.
    """
    queryset = MarketplaceListing.objects.all()
    serializer_class = MarketplaceListingSerializer
    permission_classes = [permissions.IsAuthenticated]
