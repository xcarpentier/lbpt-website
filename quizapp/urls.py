# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (
        r'^list/$',
        'quizapp.views.list_quiz',
    ),
    (
        r'^aff/(?P<key>.*)/$',
        'quizapp.views.detail_quiz',
    ),
    (
        r'^result/(?P<key>.*)/$',
        'quizapp.views.result_quiz',
    ),
)