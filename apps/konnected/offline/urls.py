# apps/konnected/offline/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from konnected.offline.views import OfflineContentPackageViewSet

router = DefaultRouter()
router.register(r'offline_packages', OfflineContentPackageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
