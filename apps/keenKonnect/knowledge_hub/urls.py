# apps/keenkonnect/knowledge_hub/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from keenkonnect.knowledge_hub.views import KnowledgeDocumentViewSet, DocumentRevisionViewSet

router = DefaultRouter()
router.register(r'knowledge_documents', KnowledgeDocumentViewSet)
router.register(r'document_revisions', DocumentRevisionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
