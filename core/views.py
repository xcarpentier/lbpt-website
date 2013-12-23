# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.conf import settings
from ragendja.template import render_to_response
from core.models import MetaData

def create_admin_user(request):
    user = User.get_by_key_name('admin')
    if not user :
        user = User(key_name='admin', username=settings.ADMIN_USERNAME,
            email=settings.DEFAULT_FROM_EMAIL, first_name=settings.ADMIN_FIRST_NAME, last_name=settings.ADMIN_LAST_NAME,
            is_active=True, is_staff=True, is_superuser=True)
        user.set_password(settings.SECRET_KEY)
        user.put()
    return render_to_response(request, 'main.html')

def site_online(request):
    query = MetaData.all()
    metadata = query.get()
    online=True
    if (metadata!=None):
        online=metadata.online
    template='main.html'
    if online!=True:
        template='main_nonline.html'
    return render_to_response(request, template)