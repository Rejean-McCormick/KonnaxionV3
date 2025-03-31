from django.urls import path, include
from rest_framework.routers import DefaultRouter
from konnaxion.core.views import (
    CustomUserViewSet,
    SystemConfigurationViewSet,
    ConfigurationChangeLogViewSet,
)

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='customuser')
router.register(r'configurations', SystemConfigurationViewSet, basename='systemconfiguration')
router.register(r'configuration-changelogs', ConfigurationChangeLogViewSet, basename='configurationchangelog')

urlpatterns = [
    path('', include(router.urls)),
]
