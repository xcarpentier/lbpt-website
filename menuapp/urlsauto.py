from django.conf.urls.defaults import *


urlpatterns = patterns('',
    (r'^m/', include('menuapp.urls')),
)
