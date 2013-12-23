from django.template import Library
from core.models import MetaData
register = Library()

@register.simple_tag
def site_name():
    query = MetaData.all()
    metadata = query.get()
    title=""
    if (metadata!=None):
        title=metadata.title
    return title