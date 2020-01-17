from django.urls import path, include
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="UPCRM API",
        default_version='v2',
        description="API for UPCRM",
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlapi = [
    path('api/v1/users/', include('users.urls')),
    path('api/v1/enums/', include('utils.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger(<format>.json|.yaml)/',
         schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('doc/', schema_view.with_ui('swagger',
                                     cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
]
urlpatterns += urlapi
