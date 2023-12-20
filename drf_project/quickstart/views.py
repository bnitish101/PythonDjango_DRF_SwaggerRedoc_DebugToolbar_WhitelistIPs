from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from quickstart.serializers import GroupSerializer, UserSerializer
from drf_project.whitelist_ip import SafelistPermission

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def initialize_request(a, request):
        # get_serializer_context = super().get_serializer_context()
        ip = get_client_ip(request)
        # print("\n\nip address: ", ip, end="\n\n")
        return super().initialize_request(request)
        # return get_serializer_context

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
