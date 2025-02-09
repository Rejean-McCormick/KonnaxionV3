# apps/keenKonnect/urls.py
from django.urls import path, include

urlpatterns = [
    path('projects/', include('keenKonnect.projects.urls')),
    path('gap_analysis/', include('keenKonnect.gap_analysis.urls')),
    path('expert_match/', include('keenKonnect.expert_match.urls')),
    path('team_formation/', include('keenKonnect.team_formation.urls')),
    path('collab_spaces/', include('keenKonnect.collab_spaces.urls')),
    path('knowledge_hub/', include('keenKonnect.knowledge_hub.urls')),
]
