# apps/kreative/marketplace/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from kreative.marketplace.views import ArtistProfileViewSet, CommissionViewSet, MarketplaceListingViewSet

router = DefaultRouter()
router.register(r'artist_profiles', ArtistProfileViewSet)
router.register(r'commissions', CommissionViewSet)
router.register(r'marketplace_listings', MarketplaceListingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
