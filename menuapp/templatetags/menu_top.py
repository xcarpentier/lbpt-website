from django.template import Library
from menuapp.models import Menu, MenuService, MenuRubrique
import logging
register = Library()

@register.inclusion_tag('menuapp/menu_top.html')
def menu_top():
    query_menu = Menu.all().filter("menu_number =",1)
    menu_top = query_menu.get()
    list_menu = []    
    if menu_top!=None:
        for menu_rubrique in MenuRubrique.all().filter('menu_rubrique_online =',True).order('menu_rubrique_prior'):        
            for menu_in in menu_rubrique.menu:
                if  Menu.get(menu_in).key() == menu_top.key():
                    item = {}
                    item['name'] = menu_rubrique.rubrique.rubrique_name
                    item['key'] = menu_rubrique.rubrique.key()
                    item['type'] = 'rubrique'
                    list_menu.append(item)

        for menu_service in MenuService.all().filter('menu_service_online =',True).order("menu_service_prior"):
            for menu_in in menu_service.menu:
                if  Menu.get(menu_in).key() == menu_top.key():
                    item = {}
                    item['name'] = menu_service.service.service_name
                    item['key'] = menu_service.service.key()
                    item['type'] = 'service'
                    list_menu.append(item)
    return {'list_menu' : list_menu}