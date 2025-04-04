# apps/konnected/community/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from konnected.konnectedcommunity.views import DiscussionThreadViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'discussions', DiscussionThreadViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
