from django.template import Library
from core.models import MetaData
register = Library()

@register.simple_tag
def site_domain_contrib():
    query = MetaData.all()
    metadata = query.get()
    domain=""
    if (metadata!=None):
        domain=metadata.domain_contrib
    return domain