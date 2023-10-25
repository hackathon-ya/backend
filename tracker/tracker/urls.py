from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

apps_url_patterns = [
    # урлы приложений
    path("", include("vacancies.urls")),
]

api_schema_url_patterns = [
    path(
        route="",
        view=SpectacularAPIView.as_view(),
        name="schema",
    ),
    path(
        route="redoc/",
        view=SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path(
        route="swagger-ui",
        view=SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]

urlpatterns = [
    path(route="api/v1/schema/", view=include(api_schema_url_patterns)),
    path(route="api/v1/", view=include(apps_url_patterns)),
    path("admin/", admin.site.urls),
]
