# -*- coding: utf-8 -*-
from google.appengine.ext import db
from core.models import Person, MetaData
from service.models import Service, Subscribe
from service.forms import SubscribeForm
from menuapp.models import Rubrique, ItemRubrique
from ragendja.template import render_to_response
from django.views.generic.list_detail import object_list, object_detail
from django.template.loader import render_to_string
import logging
from django.core.mail import send_mail
from django.conf import settings
from google.appengine.api import mail
from ragendja.dbutils import get_object
from django.contrib.auth.models import User

def subscribe_service(request, key):
    service = Service.get(key)
    form = SubscribeForm()
    person_email_content=''
    
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            type_email = form.cleaned_data['type_email']
            if service.person_mail==True:
                person_email_content = request.POST['person_mail']

            person = Person.all().filter("person_email =",email).get()
            if person==None:
                person = Person(person_first_name=first_name,person_last_name=last_name,person_email=email,
                person_is_activ=True,person_type_email=type_email)
                person.put()
            else:
                person.person_is_activ=True
                person.put()

            subscr_query = Subscribe.all().filter("subscribe_user =",person)
            result = subscr_query.get()
            inscription_new = None
            if result!=None:
                insc_exist=False
                if subscr_query.count()>1:
                    for inscription in result:
                        if inscription.subscribe_service.key()==service.key():
                            inscription.subscribe_isactive=True
                            inscription.put()
                            insc_exist=True
                else:
                    if result.subscribe_service.key()==service.key():
                        result.subscribe_isactive=True
                        result.put()
                        insc_exist=True

                if insc_exist==False:
                    inscription_new = Subscribe(subscribe_service=service,subscribe_user=person)
                    inscription_new.put()
            else:
                inscription_new = Subscribe(subscribe_service=service,subscribe_user=person)
                inscription_new.put()
            
            if service.responsable_mail==True:
                subject = render_to_string('service/subscribe_email_subject.txt',{'service': service})
                subject = ''.join(subject.splitlines())
                sender = render_to_string('service/subscribe_email_from.txt',{'metadata': MetaData.all().get()})
                message = mail.EmailMessage(sender=sender,subject=subject)
                message.body = render_to_string('service/subscribe_email.txt',{'service':service,'person':person,'msg':person_email_content})
                to = ""
                for dest in service.responsable:
                    user = get_object(User,dest)
                    to += render_to_string('service/subscribe_email_to.txt',{'user':user})
                message.to = to
                message.send()
                
            return render_to_response(request, 'service/subscribe_ok.html',{'service':service})

    return render_to_response(request, 'service/subscribe_form.html',{'service':service,'form':form})

def show_rubrique(request, key):
    rubrique = Rubrique.get(key)
    return  object_list(request, ItemRubrique.all().filter('rubrique =',rubrique.key()).order('-itemrubrique_date'),
            paginate_by=2,extra_context={'rubrique':rubrique})
