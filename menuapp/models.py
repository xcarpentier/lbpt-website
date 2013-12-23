# -*- coding: latin-1 -*-
from google.appengine.ext import db
from service.models import Service
from core.models import HTMLProperty
from ragendja.dbutils import KeyListProperty

class Menu(db.Model):
    """Menus du site"""
    menu_title = db.StringProperty(required=True,verbose_name="Titre du menu")
    menu_description = db.StringProperty(required=True,verbose_name="Description")
    menu_date = db.DateProperty(required=True,auto_now=True,verbose_name="Depuis")
    menu_number = db.IntegerProperty(required=True,verbose_name=u"Numéro du menu")
    def __unicode__(self):
        return '%s' % (self.menu_title)

class Rubrique(db.Model):
    """Rubrique : news, ..."""
    rubrique_name = db.StringProperty(required=True,verbose_name="Nom de la rubrique")
    rubrique_description = db.StringProperty(required=True,verbose_name="Description")
    rubrique_date = db.DateProperty(required=True,auto_now=True,verbose_name="Depuis")
    def __unicode__(self):
        return u'%s' % (self.rubrique_name)

class ItemRubrique(db.Model):
    """Liste des items"""
    itemrubrique_title = db.StringProperty(required=True,verbose_name="Titre")
    rubrique = db.ReferenceProperty(Rubrique,required=True,verbose_name="Rubrique")
    content = HTMLProperty(required=True,verbose_name="Contenu")
    itemrubrique_date = db.DateProperty(required=True,auto_now=True,verbose_name="Depuis")
    def __unicode__(self):
        return u'%s' % (self.itemrubrique_title)

class MenuService(db.Model):
    """Représente les services dans les menus"""
    menu = KeyListProperty(Menu)
    service = db.ReferenceProperty(Service,required=True,verbose_name="Service")
    menu_service_online = db.BooleanProperty(required=True,verbose_name="En ligne")
    menu_service_prior = db.IntegerProperty(required=True,verbose_name="Ordre")
    menu_service_pubdate = db.DateProperty(required=True,auto_now=True,verbose_name="Depuis")
    def __unicode__(self):
        return u'%s' % (self.service)

class MenuRubrique(db.Model):
    """Représente les rubriques dans les menus"""
    menu = KeyListProperty(Menu)
    rubrique = db.ReferenceProperty(Rubrique,required=True,verbose_name="Rubrique")
    menu_rubrique_online = db.BooleanProperty(required=True,verbose_name="En ligne")
    menu_rubrique_prior = db.IntegerProperty(required=True,verbose_name="Ordre")
    menu_rubrique_pubdate = db.DateProperty(required=True,auto_now=True,verbose_name="Depuis")
    def __unicode__(self):
        return u'%s' % (self.rubrique)