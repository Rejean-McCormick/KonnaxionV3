# apps/ethikos/urls.py
from django.urls import path, include

urlpatterns = [
    path('home/', include('ethikos.home.urls')),
    path('debate_arena/', include('ethikos.debate_arena.urls')),
    path('stats/', include('ethikos.stats.urls')),
    path('knowledge_base/', include('ethikos.knowledge_base.urls')),
    path('prioritization/', include('ethikos.prioritization.urls')),
    path('resolution/', include('ethikos.resolution.urls')),
]
