from django.urls import path, include
from rest_framework.routers import DefaultRouter
from konnaxion.search.views import SearchIndexViewSet, SearchQueryLogViewSet

router = DefaultRouter()
router.register(r'indexes', SearchIndexViewSet, basename='searchindex')
router.register(r'querylogs', SearchQueryLogViewSet, basename='searchquerylog')

urlpatterns = [
    path('', include(router.urls)),
]
