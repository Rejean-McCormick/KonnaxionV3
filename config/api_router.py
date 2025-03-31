"""
API Router for the Konnaxion Project

This file centralizes all API endpoints for the project. For simplicity, each
app exposes its endpoints in its own `urls.py` (instead of a separate `api/urls.py`).
"""

from django.urls import include, path

urlpatterns = [
    # Ekoh endpoints
    path("api/ekoh/", include("konnaxion.ekoh.urls")),
    
    # Debate Arena endpoints
    path("api/debate/", include("ethikos.debate_arena.urls")),
    
    # Ethikos suite of endpoints
    path("api/ethikos/home/", include("ethikos.home.urls")),
    path("api/ethikos/knowledge-base/", include("ethikos.knowledge_base.urls")),
    path("api/ethikos/prioritization/", include("ethikos.prioritization.urls")),
    path("api/ethikos/resolution/", include("ethikos.resolution.urls")),
    path("api/ethikos/stats/", include("ethikos.stats.urls")),
    
    # Keen apps endpoints
    path("api/keen/collab-spaces/", include("keenkonnect.collab_spaces.urls")),
    path("api/keen/knowledge-hub/", include("keenkonnect.knowledge_hub.urls")),
    path("api/keen/projects/", include("keenkonnect.projects.urls")),
    path("api/keen/team-formation/", include("keenkonnect.team_formation.urls")),
    
    # Konnaxion endpoints
    path("api/konnaxion/core/", include("konnaxion.core.urls")),
    path("api/konnaxion/messaging/", include("konnaxion.messaging.urls")),
    path("api/konnaxion/notifications/", include("konnaxion.notifications.urls")),
    path("api/konnaxion/search/", include("konnaxion.search.urls")),
    
    # Konnected endpoints
    path("api/konnected/foundation/", include("konnected.foundation.urls")),
    path("api/konnected/konnectedcommunity/", include("konnected.konnectedcommunity.urls")),
    path("api/konnected/learning/", include("konnected.learning.urls")),
    path("api/konnected/offline/", include("konnected.offline.urls")),
    
    # Kreative endpoints
    #path("api/kreative/core/", include("kreative.core.urls")),
    
    # Add additional endpoints here as needed.
]
