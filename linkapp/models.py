# -*- coding: latin-1 -*-
from google.appengine.ext import db
from core.models import HTMLProperty

class Link(db.Model):
    """Lien vers d'autre site"""
    link_title = db.StringProperty(required=True,verbose_name="Titre")
    content = HTMLProperty(required=True,verbose_name="Description")
    link_prior = db.IntegerProperty(required=True,verbose_name=u"Priorité")
    link_url = db.LinkProperty(required=True,verbose_name="URL")
    online = db.BooleanProperty(required=True,verbose_name="En ligne")
    class Meta:
        verbose_name = u'Lien vers autre site'
        verbose_name_plural = u'Liens vers autres sites'
    def __unicode__(self):
        return u'Lien vers : %s' % (self.link_title)