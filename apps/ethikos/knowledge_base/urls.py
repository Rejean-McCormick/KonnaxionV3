# apps/ethikos/knowledge_base/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ethikos.knowledge_base.views import DebateArchiveViewSet

router = DefaultRouter()
router.register(r'debate_archives', DebateArchiveViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
