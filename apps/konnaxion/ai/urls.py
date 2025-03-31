from django.urls import path, include
from rest_framework.routers import DefaultRouter
from konnaxion.ai.views import AIResultViewSet

router = DefaultRouter()
router.register(r'results', AIResultViewSet, basename='airesult')

urlpatterns = [
    path('', include(router.urls)),
]
