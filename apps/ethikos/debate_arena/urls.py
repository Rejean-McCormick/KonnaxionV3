# apps/ethikos/debate_arena/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ethikos.debate_arena.views import DebateSessionViewSet, ArgumentViewSet, VoteRecordViewSet

router = DefaultRouter()
router.register(r'debate_sessions', DebateSessionViewSet)
router.register(r'arguments', ArgumentViewSet)
router.register(r'vote_records', VoteRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
