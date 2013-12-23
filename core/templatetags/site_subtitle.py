from django.template import Library
from core.models import MetaData
register = Library()

@register.simple_tag
def site_subtitle():
    query = MetaData.all()
    metadata = query.get()
    subtitle=""
    if (metadata!=None):
        subtitle=metadata.sub_title
    return subtitle