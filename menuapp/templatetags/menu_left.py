from django.template import Library
from menuapp.models import Menu, MenuService, MenuRubrique
import logging
register = Library()

@register.inclusion_tag('menuapp/menu_left.html')
def menu_left():
    query_menu = Menu.all().filter("menu_number >",1)
    menu_left_list = query_menu.get()
    list_menus = []
    if menu_left_list != None:
        if query_menu.count()>1:
            for menu_left in query_menu:
                list_item = []
                for menu_rubrique in MenuRubrique.all().filter('menu_rubrique_online =',True).order('menu_rubrique_prior'):        
                    for menu_in in menu_rubrique.menu:
                        if  Menu.get(menu_in).key() == menu_left.key():
                            item = {}
                            item['name'] = menu_rubrique.rubrique.rubrique_name
                            item['key'] = menu_rubrique.rubrique.key()
                            item['type'] = 'rubrique'
                            list_item.append(item)

                for menu_service in MenuService.all().filter('menu_service_online =',True).order("menu_service_prior"):
                    for menu_in in menu_service.menu:
                        if  Menu.get(menu_in).key() == menu_left.key():
                            item = {}
                            item['name'] = menu_service.service.service_name
                            item['key'] = menu_service.service.key()
                            item['type'] = 'service'
                            list_item.append(item)
                group={}
                group['name'] = menu_left.menu_title
                group['values'] = list_item
                list_menus.append(group)
        else:
            list_item = []
            for menu_rubrique in MenuRubrique.all().filter('menu_rubrique_online =',True).order('menu_rubrique_prior'):        
                for menu_in in menu_rubrique.menu:
                    if  Menu.get(menu_in).key() == menu_left_list.key():
                        item = {}
                        item['name'] = menu_rubrique.rubrique.rubrique_name
                        item['key'] = menu_rubrique.rubrique.key()
                        item['type'] = 'rubrique'
                        list_item.append(item)

            for menu_service in MenuService.all().filter('menu_service_online =',True).order("menu_service_prior"):
                for menu_in in menu_service.menu:
                    if  Menu.get(menu_in).key() == menu_left_list.key():
                        item = {}
                        item['name'] = menu_service.service.service_name
                        item['key'] = menu_service.service.key()
                        item['type'] = 'service'
                        list_item.append(item)
            group={}
            group['name'] = menu_left_list.menu_title
            group['values'] = list_item
            list_menus.append(group)
            
    return {'list_menus' : list_menus}