# -*- coding: latin-1 -*-
from google.appengine.ext import db
from django.contrib.auth.models import User
from core.models import HTMLProperty

class Agenda(db.Model):
    title_event = db.StringProperty(required=True,verbose_name=u"Titre de l'�v�nement")
    agenda_startdate = db.DateTimeProperty(required=True,verbose_name=u"D�but")
    agenda_enddate = db.DateTimeProperty(required=True,verbose_name="Fin")
    agenda_lieux = db.PostalAddressProperty(required=True,verbose_name=u"Lieux de l'�v�nement")
    content = HTMLProperty(required=True,verbose_name=u"Description")
    agenda_online = db.BooleanProperty(required=True,verbose_name="En ligne")
    agenda_contact = db.ReferenceProperty(User,required=True,verbose_name="Contact")
    def __unicode__(self):
        return u'Ev�nemenet : %s (d�but: %s, fin: %s)' % (self.title_event, self.agenda_startdate,self.agenda_startdate)

