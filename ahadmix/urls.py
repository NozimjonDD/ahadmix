from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.static import serve as static_serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('common.urls', namespace='common')),
]

if settings.DEBUG:
    docs_root = settings.BASE_DIR / 'docs'
    urlpatterns += [
        path(
            'videos/<path:path>',
            static_serve,
            {'document_root': docs_root / 'videos'},
        ),
        path(
            'AHADMIX-KP-2026.pdf',
            static_serve,
            {'path': 'AHADMIX-KP-2026.pdf', 'document_root': docs_root},
        ),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
