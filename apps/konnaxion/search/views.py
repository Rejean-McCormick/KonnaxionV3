from rest_framework import viewsets, permissions
from konnaxion.search.models import SearchIndex, SearchQueryLog
from konnaxion.search.serializers import SearchIndexSerializer, SearchQueryLogSerializer

class SearchIndexViewSet(viewsets.ModelViewSet):
    """
    Endpoints pour gérer la configuration des index de recherche.
    """
    queryset = SearchIndex.objects.all()
    serializer_class = SearchIndexSerializer
    permission_classes = [permissions.IsAuthenticated]

class SearchQueryLogViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Endpoints en lecture seule pour consulter les journaux des requêtes de recherche.
    """
    queryset = SearchQueryLog.objects.all()
    serializer_class = SearchQueryLogSerializer
    permission_classes = [permissions.IsAuthenticated]
