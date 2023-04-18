from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("contract.urls")),
    path("", include("accounts.urls")),
    path("media/contracts/<path:path>", serve, {"document_root": settings.MEDIA_ROOT}),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
