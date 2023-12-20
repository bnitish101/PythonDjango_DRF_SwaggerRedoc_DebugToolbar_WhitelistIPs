from rest_framework import permissions
from django.conf import settings

from pathlib import Path 

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'. 
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent 

# Reading env file 
env = environ.Env() 
# environ.Env.read_env(osp.join(BASE_DIR.parent, ".env"))


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