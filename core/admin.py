# -*- coding: latin-1 -*-
from django.contrib import admin
from core.models import MetaData, Homepage, Person

class MetaDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title','online','dateonline')

class HomepageAdmin(admin.ModelAdmin):
    list_display = ('title', 'dateonline')
    
class PersonAdmin(admin.ModelAdmin):
    list_display = ('person_first_name', 'person_last_name','person_email','person_is_activ','person_date_crea')

admin.site.register(MetaData, MetaDataAdmin)
admin.site.register(Homepage, HomepageAdmin)
admin.site.register(Person, PersonAdmin)
