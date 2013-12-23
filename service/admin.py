# -*- coding: latin-1 -*-
from django.contrib import admin
from service.models import Service, Subscribe

class ServiceAdmin(admin.ModelAdmin):
   list_display = ('service_name','service_date')
   exclude = ('service_date',)

class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('subscribe_service','subscribe_user','subscribe_date','subscribe_isactive')

admin.site.register(Service, ServiceAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
