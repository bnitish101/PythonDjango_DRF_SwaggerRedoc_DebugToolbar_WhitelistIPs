"""
URL configuration for drf_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin


from django.urls import include, path
from rest_framework import routers

from quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# ------ cb+ s (debug toolbar) ------ #
urlpatterns += [
    path("__debug__/", include("debug_toolbar.urls")),
]
# ------ cb+ e (debug toolbar) ------ #


# ------ cb+ s (swagger specification or OpenApi Specification) ------ #
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="DRF with swagger/openApi specification",
        default_version="v1",
        description="Demo for swagger specifiaction or OpenApi Specification with DRF",
        terms_of_service="https://www.google.com",
        contact=openapi.Contact(email="abc@example.com"),
        license=openapi.License(name="Open Source"),
    ),
    public=True,
    # permission_classes=(permissions.allowAny,),
)
urlpatterns += [
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path("redoc/", schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc-ui'
    ),
]
# ------ cb+ e (swagger specification or OpenApi Specification) ------ #



urlpatterns += router.urls
