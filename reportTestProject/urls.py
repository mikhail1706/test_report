from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('reports/', include('reports.urls')),

    path('swagger-ui/', TemplateView.as_view(template_name='swagger-ui.html',
                                             extra_context={'schema_url': 'openapi-schema'}), name='swagger-ui'),
    path('openapi', get_schema_view(title="Your Project", description="API for all things …", version="1.0.0"),
         name='openapi-schema'),

    path('admin/', admin.site.urls),
]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
