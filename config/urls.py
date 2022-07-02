from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("allauth.urls")),
    path("", include("djangoblog.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
if settings.DEBUG:
    import debug_toolbar  # noqa: F401  # pragma: no cover

    urlpatterns = [  # pragma: no cover
        path("__debug__/", include("debug_toolbar.urls")),
    ] + urlpatterns
"""
