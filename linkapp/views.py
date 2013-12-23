# -*- coding: utf-8 -*-
from django.views.generic.list_detail import object_list, object_detail
from linkapp.models import Link

def list_link(request):
    return  object_list(request, Link.all().filter('online =',True).order('link_prior'),
            paginate_by=10)
