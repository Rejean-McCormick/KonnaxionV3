# apps/keenkonnect/gap_analysis/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from keenkonnect.gap_analysis.views import GapAnalysisViewSet

router = DefaultRouter()
router.register(r'gap_analyses', GapAnalysisViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
