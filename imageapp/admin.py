# -*- coding: latin-1 -*-
from django.contrib import admin
from imageapp.models import Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    exclude = ('created','encoding',)

admin.site.register(Image, ImageAdmin)