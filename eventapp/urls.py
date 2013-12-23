from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (
        r'^list/$',
        'eventapp.views.list_agenda',
    ),
    (
        r'^(?P<key>.*)/$',
        'eventapp.views.detail_agenda'
    ),
    
)
