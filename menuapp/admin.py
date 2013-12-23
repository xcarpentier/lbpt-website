# -*- coding: latin-1 -*-
from django.contrib import admin
from menuapp.models import Menu, Rubrique, ItemRubrique,MenuService, MenuRubrique

class MenuAdmin(admin.ModelAdmin):
   list_display = ('menu_title','menu_number','menu_description','menu_date')
   exclude = ('menu_date',)

class RubriqueAdmin(admin.ModelAdmin):
    list_display = ('rubrique_name','rubrique_description','rubrique_date')
    exclude = ('rubrique_date',)

class ItemRubriqueAdmin(admin.ModelAdmin):
    list_display = ('itemrubrique_title','rubrique','itemrubrique_date')
    list_filter = ('rubrique', 'content')
    exclude = ('itemrubrique_date',)

class MenuServiceAdmin(admin.ModelAdmin):
    list_display = ('service','menu_service_online','menu_service_prior','menu_service_pubdate')
    list_filter = ('service','menu_service_online')
    exclude = ('menu_service_pubdate',)

class MenuRubriqueAdmin(admin.ModelAdmin):
    list_display = ('rubrique','menu_rubrique_online','menu_rubrique_prior','menu_rubrique_pubdate')
    list_filter = ('rubrique','menu_rubrique_online')
    exclude = ('menu_rubrique_pubdate',)

admin.site.register(Menu,MenuAdmin)
admin.site.register(Rubrique, RubriqueAdmin)
admin.site.register(ItemRubrique, ItemRubriqueAdmin)
admin.site.register(MenuService, MenuServiceAdmin)
admin.site.register(MenuRubrique, MenuRubriqueAdmin)
