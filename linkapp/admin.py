# -*- coding: latin-1 -*-
from django.contrib import admin
from linkapp.models import Link

class LinkAdmin(admin.ModelAdmin):
    list_display = ('link_title', 'link_url','online')

admin.site.register(Link, LinkAdmin)