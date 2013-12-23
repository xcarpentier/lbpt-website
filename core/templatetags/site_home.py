from django.template import Library
from core.models import Homepage
register = Library()

@register.inclusion_tag('core/home.html')
def site_home():
    query = Homepage.all()
    home = query.get()
    if(home==None or home.online!=True):
        home =  Homepage(title="Bienvenue",content="Bienvenu sur ce site !")
    return {'home':home}