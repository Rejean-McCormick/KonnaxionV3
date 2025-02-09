# konnaxion_project/config/api_router.py

"""
API Router for the Konnaxion Project

This file centralizes all API endpoints for the project. For simplicity, each
app exposes its endpoints in its own `urls.py` (instead of a separate `api/urls.py`).
"""

from django.urls import include, path

urlpatterns = [
    # Ekoh endpoints
    path("api/ekoh/", include("konnaxion_project.ekoh.urls")),
    
    # Debate Arena endpoints
    path("api/debate/", include("konnaxion_project.debate_arena.urls")),
    
    # Ethikos suite of endpoints
    path("api/ethikos/home/", include("konnaxion_project.ethikos_home.urls")),
    path("api/ethikos/knowledge-base/", include("konnaxion_project.ethikos_knowledge_base.urls")),
    path("api/ethikos/prioritization/", include("konnaxion_project.ethikos_prioritization.urls")),
    path("api/ethikos/resolution/", include("konnaxion_project.ethikos_resolution.urls")),
    path("api/ethikos/stats/", include("konnaxion_project.ethikos_stats.urls")),
    
    # Keen apps endpoints
    path("api/keen/collab-spaces/", include("konnaxion_project.keen_collab_spaces.urls")),
    path("api/keen/knowledge-hub/", include("konnaxion_project.keen_knowledge_hub.urls")),
    path("api/keen/projects/", include("konnaxion_project.keen_projects.urls")),
    path("api/keen/team-formation/", include("konnaxion_project.keen_team_formation.urls")),
    
    # Konnaxion endpoints
    #path("api/konnaxion/ai/", include("konnaxion_ai.urls")),
    path("api/konnaxion/core/", include("konnaxion_project.konnaxion_core.urls")),
    path("api/konnaxion/messaging/", include("konnaxion_project.konnaxion_messaging.urls")),
    path("api/konnaxion/notifications/", include("konnaxion_project.konnaxion_notifications.urls")),
    path("api/konnaxion/search/", include("konnaxion_project.konnaxion_search.urls")),
    
    # Konnected endpoints
    path("api/konnected/foundation/", include("konnaxion_project.konnected_foundation.urls")),
    path("api/konnected/community/", include("konnaxion_project.konnected_community.urls")),
    path("api/konnected/learning/", include("konnaxion_project.konnected_learning.urls")),
    path("api/konnected/offline/", include("konnaxion_project.konnected_offline.urls")),
    
    # Kreative endpoints
    path("api/kreative/core/", include("konnaxion_project.kreative_core.urls")),
    
    # Add additional endpoints here as needed.
]
