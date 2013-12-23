# -*- coding: utf-8 -*-
from django.views.generic.list_detail import object_list, object_detail
from eventapp.models import Agenda

def list_agenda(request):
    return  object_list(request, Agenda.all().filter('agenda_online =',True).order('-agenda_startdate'),
            paginate_by=3)

def detail_agenda(request,key):
    return  object_detail(request, Agenda.all(),key)
