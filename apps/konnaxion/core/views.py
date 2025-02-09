from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.konnaxion.core.models import CustomUser, SystemConfiguration, ConfigurationChangeLog
from apps.konnaxion.core.serializers import (
    CustomUserSerializer,
    SystemConfigurationSerializer,
    ConfigurationChangeLogSerializer
)
# Exemple : Importer une tâche asynchrone pour consigner les changements de configuration
# from apps.konnaxion.core.tasks import log_configuration_change

class CustomUserViewSet(viewsets.ModelViewSet):
    """
    Endpoints pour la gestion des utilisateurs (CustomUser).
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def update_profile(self, request, pk=None):
        """
        Action personnalisée pour mettre à jour le profil utilisateur.
        (Ici, vous pouvez déclencher un événement asynchrone pour la synchronisation offline ou la notification.)
        """
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # Exemple : Déclencher une tâche asynchrone pour notifier la mise à jour
        # tasks.trigger_user_update_event.delay(user.id)
        return Response(serializer.data)

class SystemConfigurationViewSet(viewsets.ModelViewSet):
    """
    Endpoints pour la gestion de la configuration système.
    Toute modification peut déclencher un enregistrement asynchrone dans l’historique.
    """
    queryset = SystemConfiguration.objects.all()
    serializer_class = SystemConfigurationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        instance = serializer.save()
        # Exemple : Déclencher une tâche asynchrone pour enregistrer le changement
        # log_configuration_change.delay(instance.id)

class ConfigurationChangeLogViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Endpoint en lecture seule pour consulter l’historique des modifications de configuration.
    """
    queryset = ConfigurationChangeLog.objects.all()
    serializer_class = ConfigurationChangeLogSerializer
    permission_classes = [permissions.IsAuthenticated]
