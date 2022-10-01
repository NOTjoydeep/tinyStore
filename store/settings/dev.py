from .common import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bcd)&ky!qs9qd_clo5nxe=6hr_a_u@aoq79nzlay57pqe3@#ho'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'store3',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Admin@123'
    }
}

