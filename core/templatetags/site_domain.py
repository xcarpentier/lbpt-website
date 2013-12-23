from django.template import Library
from core.models import MetaData
register = Library()

@register.simple_tag
def site_domain():
    query = MetaData.all()
    metadata = query.get()
    domain=""
    if (metadata!=None):
        domain=metadata.domain
    return domain