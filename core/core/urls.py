
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1+v2',
      description="this is a test api for advance django course project",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="bahmanpn@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('blog/',include('blog.urls')),
    path('accounts/',include('accounts.urls')),
    path('api/',include('api.urls')),
    #api-doc
    path('api-docs/',include_docs_urls(title='api docs')),
    #drf-yasg
    path('swagger/output.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/output.yaml', schema_view.without_ui(cache_timeout=0), name='schema-yaml'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
