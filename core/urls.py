# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from core.views import create_admin_user

urlpatterns = patterns('',
    (r'^start/$', create_admin_user),
)
