# -*- coding: latin-1 -*-
from ragendja.settings_pre import *

MEDIA_VERSION = 1
#DEBUG = False
COMBINE_MEDIA = {
    'combined-%(LANGUAGE_DIR)s.css': (
        'global/css/style.css',
    ),
}

if on_production_server:
    DEFAULT_FROM_EMAIL = 'carpentier.xavierrachel@gmail.com'
    SERVER_EMAIL = DEFAULT_FROM_EMAIL

SECRET_KEY = 'g6mbdfh'

#ENABLE_PROFILER = True
#ONLY_FORCED_PROFILE = True
#PROFILE_PERCENTAGE = 25
#SORT_PROFILE_RESULTS_BY = 'cumulative' # default is 'time'
# Profile only datastore calls
#PROFILE_PATTERN = 'ext.db..+\((?:get|get_by_key_name|fetch|count|put)\)'

# Enable I18N and set default language to 'en'
USE_I18N = True
LANGUAGE_CODE = 'en'

# Restrict supported languages (and JS media generation)
LANGUAGES = (
    ('fr', 'French'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'ragendja.middleware.ErrorMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'ragendja.sites.dynamicsite.DynamicSiteIDMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
)

LOGIN_URL = '/account/login/'
LOGOUT_URL = '/account/logout/'
LOGIN_REDIRECT_URL = '/'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.admin',
    'appenginepatcher',
    'ragendja',
    'mediautils',
    'tinymce',
    'core',
    'service',
    'menuapp',
    'eventapp',
    'linkapp',
    'imageapp',
    'quizapp',
)

# List apps which should be left out from app settings and urlsauto loading
IGNORE_APP_SETTINGS = IGNORE_APP_URLSAUTO = (
    # Example:
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    # 'yetanotherapp',
)

# Remote access to production server (e.g., via manage.py shell --remote)
DATABASE_OPTIONS = {
    # Override remoteapi handler's path (default: '/remote_api').
    # This is a good idea, so you make it not too easy for hackers. ;)
    # Don't forget to also update your app.yaml!
    #'remote_url': '/remote-secret-url',

    # !!!Normally, the following settings should not be used!!!

    # Always use remoteapi (no need to add manage.py --remote option)
    #'use_remote': True,

    # Change appid for remote connection (by default it's the same as in
    # your app.yaml)
    #'remote_id': 'otherappid',

    # Change domain (default: <remoteid>.appspot.com)
    #'remote_host': 'bla.com',
}

TINYMCE_JS_URL='/static/js/tiny_mce/tiny_mce.js'
TINYMCE_DEFAULT_CONFIG={'theme': "advanced",
    'theme_advanced_toolbar_location' : "top",
    'theme_advanced_toolbar_align' : "left",
    'theme_advanced_buttons1' : "fullscreen,bold,italic,underline,strikethrough,justifyleft,justifycenter,justifyright,justifyfull,bullist,numlist,outdent,indent,undo,redo,link,unlink,anchor,image,forecolor",
    'theme_advanced_buttons2' : "fontsizeselect,formatselect,code",
    'theme_advanced_buttons3' : "",
    'auto_cleanup_word' : "true",
    'plugins' : "fullscreen,advimage",
}

ADMIN_FIRST_NAME='xavier'
ADMIN_LAST_NAME='carpentier'
ADMIN_USERNAME='xcarpentier'

from ragendja.settings_post import *
