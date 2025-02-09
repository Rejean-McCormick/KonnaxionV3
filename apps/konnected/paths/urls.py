# apps/konnected/paths/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from konnected.paths.views import LearningPathViewSet, PathStepViewSet

router = DefaultRouter()
router.register(r'learning_paths', LearningPathViewSet)
router.register(r'path_steps', PathStepViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
