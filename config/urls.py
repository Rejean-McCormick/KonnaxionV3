# konnaxion_project/config/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from konnaxion.views import debug_test 



# Import API URLs
from .api_router import urlpatterns as api_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(api_urlpatterns)),  # Includes your API URLs
    path('api/v1/konnaxion/', include('konnaxion.urls')),
    path('api/v1/konnected/', include('konnected.urls')),
    path('api/v1/keenkonnect/', include('keenkonnect.urls')),
    path('api/v1/ethikos/', include('ethikos.urls')),
    path('api/v1/kreative/', include('kreative.urls')),
    path("debug-test/", debug_test, name="debug-test"),
]
# Add Django Debug Toolbar URLs only in development mode
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]