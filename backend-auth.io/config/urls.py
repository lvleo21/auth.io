from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings

from .settings.swagger import schema_view
from apps.core.sites import custom_admin_site


urlpatterns = [
    # Unfold Admin
    path("staff/", custom_admin_site.urls),

    # Debug Toolbar
    path("__debug__/", include("debug_toolbar.urls")),

    # Rosetta
    re_path(r'^rosetta/', include('rosetta.urls')),

    # Swagger
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc"
    ),

    # Media
    re_path(
        r'^media/(?P<path>.*)$',
        serve,
        {'document_root': settings.MEDIA_ROOT}
    ),

    # Static
    re_path(
        r'^static/(?P<path>.*)$',
        serve,
        {'document_root': settings.STATIC_ROOT}
    ),
]
