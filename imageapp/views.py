import logging
import time

from django.http import HttpResponse, Http404
from django.utils.http import http_date
from django.views.generic.list_detail import object_list
from google.appengine.api import images
from google.appengine.ext import db
from ragendja.auth.decorators import staff_only

from imageapp.models import Image

def serve_image(
        request, image,
        width=None, height=None, encoding=None,
        last_modified=None, use_etag=False
    ):
    if not image:
        raise Http404
    response = HttpResponse(image.image_bytes, image.mime_type)
    if last_modified is None:
        last_modified = time.mktime(image.created.timetuple())
    response['Last-Modified'] = http_date(epoch_seconds=last_modified)
    return response

def serve(request, image_key, width=None, height=None, extension='png'):
    encoding = None
    if extension.lower() == 'jpg' or extension.lower() == 'jpeg':
        encoding = images.JPEG
    if extension.lower() == 'png':
        encoding = images.PNG
    if encoding is None:
        raise Http404
    image = Image.get(db.Key(encoded=image_key))
    return serve_image(
        request, image,
        width=width, height=height, encoding=encoding
    )

@staff_only
def list_images(request):
    return object_list(request, Image.all(),paginate_by=5)