# apps/konnected/foundation/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from konnected.foundation.views import KnowledgeUnitViewSet

router = DefaultRouter()
router.register(r'knowledge_units', KnowledgeUnitViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
