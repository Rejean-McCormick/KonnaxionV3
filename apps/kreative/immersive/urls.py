# apps/kreative/immersive/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from kreative.immersive.views import ImmersiveExperienceViewSet

router = DefaultRouter()
router.register(r'immersive_experiences', ImmersiveExperienceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
