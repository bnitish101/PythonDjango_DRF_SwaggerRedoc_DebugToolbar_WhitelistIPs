Integration of Debug Toolbar with django
- Only two steps

1. Add code in project settings.py file
# ------ cb+ s (debug toolbar) ------ #
INSTALLED_APPS += [
    "debug_toolbar"
]
MIDDLEWARE += [
    # ...
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # ...
]
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
# ------ cb+ e (debug toolbar) ------ #

2. Add code in project urls.py
# ------ cb+ s (debug toolbar) ------ #
urlpatterns += [
    path("__debug__/", include("debug_toolbar.urls")),
]
# ------ cb+ e (debug toolbar) ------ #



Integration of Swagger Specification or OpenApi Specification with DRF
- Only two steps

1. Add code in project settings.py file
# ------ cb+ s (swagger specification or OpenApi Specification) ------ #
INSTALLED_APPS +=[
    "drf_yasg",
]
# ------ cb+ e (swagger specification or OpenApi Specification) ------ #

2. Add code in project urls.py
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

# ------ cb+ s (whitelist IPs) ------ #
#create a class for whitelist, this class overrides has_permission method and fetch the ip from request, if ip is found then return True else False.
class SafelistPermission(permissions.BasePermission):
    """
    Ensure the request's IP address is on the safe list configured in Django settings.
    """

    def has_permission(self, request, view):
        WHITELIST_IPS = env.bool("WHITELIST_IPS", False) 

        remote_addr = request.META['REMOTE_ADDR']
        if WHITELIST_IPS:
            print(f"{remote_addr} found in whitelist ips.")
        else:
            print(f"{remote_addr} not found in whitelist ips.")
        for valid_ip in settings.REST_SAFE_LIST_IPS:
            if remote_addr == valid_ip or remote_addr.startswith(valid_ip):
                return True

        return False

# add into settings.py REST_FRAMEWORK DEFAULT_PERMISSION_CLASSES, this will call on settings.py load.
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'drf_project.whitelist_ip.SafelistPermission',   # see REST_SAFE_LIST_IPS
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
# ------ cb+ e (whitelist IPs) ------ #