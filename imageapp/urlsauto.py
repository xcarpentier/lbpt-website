from django.conf.urls.defaults import *


urlpatterns = patterns('',
    (r'^get/', include('imageapp.urls')),
)
