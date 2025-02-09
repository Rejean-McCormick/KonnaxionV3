# apps/ethikos/resolution/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ethikos.resolution.views import DebateResolutionViewSet

router = DefaultRouter()
router.register(r'debate_resolutions', DebateResolutionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
