import logging
from StringIO import StringIO
import struct

from django.db.models import permalink
from google.appengine.api import images, urlfetch
from google.appengine.ext import db

try:
    import png
except ImportError:
    png = None

class Image(db.Model):
    name = db.StringProperty(required=True,verbose_name=u"Nom de l'image")
    image_bytes = db.BlobProperty(required=True,verbose_name="Image")
    created = db.DateTimeProperty(auto_now_add=True,required=True)
    encoding = db.IntegerProperty(required=False)
    
    def __unicode__(self):
        return self.name
    
    def get_mime_type(self):
        return 'image/png' if self.encoding == images.PNG else 'image/jpeg'
    mime_type = property(get_mime_type)
    
