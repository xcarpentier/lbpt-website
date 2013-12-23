from django.conf.urls.defaults import *

urlpatterns = patterns(
    '',
    url(
        r'^(?P<image_key>.*)\.(?P<extension>.*)$',
        'imageapp.views.serve',
        name='image_serve'
    ),
    url(
        r'^all_images.*$',
        'imageapp.views.list_images',
        name='admin_images'
    )
)
