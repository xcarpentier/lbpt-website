# -*- coding: latin-1 -*-
from google.appengine.ext import db
from core.models import Person
from django.contrib.auth.models import User
from core.models import HTMLProperty
from ragendja.dbutils import KeyListProperty

class Service(db.Model):
    """Services du site"""
    class Meta:
        verbose_name = u'Service fournit par le site'
        verbose_name_plural = u'Services fournient par le site'
    service_name = db.StringProperty(required=True,verbose_name="Nom du service")
    content = HTMLProperty(required=True,verbose_name="Description")
    service_date = db.DateProperty(required=True,auto_now=True,verbose_name="Depuis")
    person_mail = db.BooleanProperty(default=False,verbose_name=u"Message avec saisie de texte de l'internaute ?")
    responsable_mail = db.BooleanProperty(default=False,verbose_name=u"Envoyer un email au responsable du service ?")
    responsable = KeyListProperty(User)
    def __unicode__(self):
        return u'%s' % (self.service_name)

class Subscribe(db.Model):
    """Contient les inscriptions aux services"""
    class Meta:
        verbose_name = u'Inscription à un service du site'
        verbose_name_plural = u'Inscriptions des internautes aux services du site'
    subscribe_service = db.ReferenceProperty(Service,verbose_name=u"Service")
    subscribe_user = db.ReferenceProperty(Person,verbose_name=u"Inscrit")
    subscribe_date = db.DateProperty(auto_now=True,verbose_name=u"Date inscription")
    subscribe_isactive = db.BooleanProperty(default=True,verbose_name=u"Actif")
    def __unicode__(self):
        return u'%s->%s' % (self.subscribe_user,self.subscribe_service)
