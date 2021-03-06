from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    # DJANGO APPS
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    
    # CUSTOM APPS
    path('', include('apps.core.urls')),
    path('departamentos/', include('apps.departamentos.urls')),
    path('documentos/', include('apps.documentos.urls')),
    path('empresas/', include('apps.empresas.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('horas-extras/', include('apps.registro_hora_extra.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
