# -*- coding: latin-1 -*-
from google.appengine.ext import db
from django.contrib.admin import widgets as admin_widgets
from tinymce import widgets as tinymce_widgets

class HTMLProperty(db.TextProperty):
    def formfield(self, **kwargs):
        defaults = {'widget': tinymce_widgets.TinyMCE}
        defaults.update(kwargs)
        if defaults['widget'] == admin_widgets.AdminTextareaWidget:
            defaults['widget'] = tinymce_widgets.AdminTinyMCE
        return super(HTMLProperty, self).formfield(**defaults)

class MetaData(db.Model):
    title = db.StringProperty(required=True)
    sub_title = db.StringProperty(required=True)
    adresse = db.PostalAddressProperty(required=True)
    contact = db.StringProperty(required=True)
    email1 = db.EmailProperty(required=True)
    email2 = db.EmailProperty(required=True)
    default_from_email = db.EmailProperty(required=True)
    domain = db.LinkProperty(required=True)
    domain_contrib = db.LinkProperty(required=True)
    phone = db.PhoneNumberProperty(required=True)
    online = db.BooleanProperty()
    dateonline = db.DateProperty(required=True,auto_now=True)
    def __unicode__(self):
        return u'Données globales : %s %s' % (self.title, self.domain)

class Homepage(db.Model):
    title = db.StringProperty(required=True,verbose_name="Titre")
    content = HTMLProperty(required=True,verbose_name="Contenu")
    dateonline = db.DateProperty(auto_now=True)
    online = db.BooleanProperty()
    def __unicode__(self):
        return u'Homepage : %s' % (self.title)

class Person(db.Model):
    person_first_name = db.StringProperty(required=True,verbose_name=u"Prénom")
    person_last_name = db.StringProperty(required=True,verbose_name=u"Nom")
    person_email = db.EmailProperty(required=True,verbose_name=u"Email")
    person_is_activ = db.BooleanProperty(verbose_name=u"Actif")
    person_date_crea = db.DateTimeProperty(required=True,auto_now=True,verbose_name=u"Date de création")
    person_type_email = db.StringProperty(choices=('HTML','TEXT'),required=False,verbose_name=u"Type email")
    def __unicode__(self):
        return u'%s %s (%s)' % (self.person_first_name, self.person_last_name,self.person_email)

class StatParam(db.Model):
    statparam_fonction = db.StringProperty(required=True)
    statparam_etape = db.StringProperty(required=True)

class StatsSites(db.Model):
    statparam = db.ReferenceProperty(StatParam,required=True)
    stat_when = db.DateTimeProperty(required=True,auto_now=True)
    stat_user = db.ReferenceProperty(required=False)
