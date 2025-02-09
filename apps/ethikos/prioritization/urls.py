# apps/ethikos/prioritization/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ethikos.prioritization.views import DebatePrioritizationViewSet

router = DefaultRouter()
router.register(r'debate_prioritizations', DebatePrioritizationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
