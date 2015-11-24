__author__ = 'viresh'

from rest_framework.permissions import  BasePermission
from django.contrib.auth.models import Group

######### Permission Classes #########

class IsNormalUser(BasePermission):
    def has_permission(self, request, view):
        usergrp = Group.objects.get(name='user')
        if usergrp in request.user.groups.all() and request.method != 'GET':
            return False
        return True




