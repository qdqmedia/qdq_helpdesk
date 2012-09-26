import os

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

DEBUG = TEMPLATE_DEBUG = True

ADMINS = (
    ('QDQ tech', 'tecnologia@qdqmedia.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'qdqhelpdesk',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Europe/Madrid'

LANGUAGE_CODE = 'es'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media/')

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static_collected/')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
	os.path.join(PROJECT_ROOT, 'static/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '89u17t2-zrv*q!06^ka7ga(bf2+=v@c32s6a+l6!_=bq#y#-^1'

QDQAUTHMIDDLEWARE = {
    'secret_keyword': 'CMSDJANGO',
    'url_login': 'http://login.apps.qdqmedia.com/index.php',
    'create_user': True,
    'program_id': 'CMS',
    'caption': 'CMS',
    'url_path_return': 'helpdesk_home',
    'url_path_index' : 'helpdesk_home'
}


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django_qdqauth.login.QDQAuthMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'qdq_helpdesk.urls'

WSGI_APPLICATION = 'qdq_helpdesk.wsgi.application'

TEMPLATE_DIRS = (

	os.path.join(PROJECT_ROOT, 'templates/'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # 'django.contrib.admindocs',
    # Third-party apps.
	'django_extensions',
    'south',
    'widget_tweaks',
    'helpdesk',
    'django_qdqauth',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
