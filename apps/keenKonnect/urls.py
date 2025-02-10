# apps/keenkonnect/urls.py
from django.urls import path, include

urlpatterns = [
    path('projects/', include('keenkonnect.projects.urls')),
    path('gap_analysis/', include('keenkonnect.gap_analysis.urls')),
    path('expert_match/', include('keenkonnect.expert_match.urls')),
    path('team_formation/', include('keenkonnect.team_formation.urls')),
    path('collab_spaces/', include('keenkonnect.collab_spaces.urls')),
    path('knowledge_hub/', include('keenkonnect.knowledge_hub.urls')),
]
