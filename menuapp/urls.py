from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(
        r'^ser/(?P<key>.*)$',
        'menuapp.views.subscribe_service',
    ),
    url(
        r'^rub/(?P<key>.*)$',
        'menuapp.views.show_rubrique',
    ),
)
