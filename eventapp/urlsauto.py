from django.conf.urls.defaults import *

rootpatterns = patterns('',
    (r'^agenda/', include('eventapp.urls')),
)
