# apps/ethikos/stats/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ethikos.stats.views import DebateStatisticViewSet, DebateEventLogViewSet

router = DefaultRouter()
router.register(r'debate_statistics', DebateStatisticViewSet)
router.register(r'debate_event_logs', DebateEventLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
