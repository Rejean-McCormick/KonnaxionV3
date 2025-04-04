# apps/keenkonnect/collab_spaces/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from keenkonnect.collab_spaces.views import CollabSpaceViewSet, DocumentViewSet, ChatMessageViewSet

router = DefaultRouter()
router.register(r'collab_spaces', CollabSpaceViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'chat_messages', ChatMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
