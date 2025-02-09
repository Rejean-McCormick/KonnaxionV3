# apps/konnaxion/urls.py

from django.urls import path, include

urlpatterns = [
    path('core/', include('konnaxion.core.urls')),             # URL pour l'app core (utilisateurs, configuration, etc.)
    path('search/', include('konnaxion.search.urls')),           # URL pour l'app search
    path('ai/', include('konnaxion.ai.urls')),                   # URL pour l'app ai
    path('notifications/', include('konnaxion.notifications.urls')),  # URL pour l'app notifications
    path('messaging/', include('konnaxion.messaging.urls')),     # URL pour l'app messaging
    path('ekoh/', include('konnaxion.ekoh.urls')),               # URL pour l'app ekoh (moteur de réputation)
]
