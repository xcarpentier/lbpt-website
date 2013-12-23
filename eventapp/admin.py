# -*- coding: latin-1 -*-
from django.contrib import admin
from eventapp.models import Agenda

class AgendaAdmin(admin.ModelAdmin):
    list_display = ('title_event', 'agenda_startdate','agenda_enddate','agenda_lieux','agenda_online','agenda_contact',)
    list_filter = ('agenda_startdate', 'agenda_contact','agenda_lieux','agenda_online')

admin.site.register(Agenda, AgendaAdmin)