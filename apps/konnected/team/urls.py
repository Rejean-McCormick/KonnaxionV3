# apps/konnected/team/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from konnected.team.views import TeamViewSet, TeamInvitationViewSet

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'invitations', TeamInvitationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
