"""
Django production settings
"""
from email.policy import default

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Production hosts (update these for your domain)
ALLOWED_HOSTS = [
    'your-domain.com',
    'www.your-domain.com',
    '*.elasticbeanstalk.com',  # If using AWS Elastic Beanstalk
    '*.amazonaws.com',
    '127.0.0.1',
    'localhost',
    "*"
]

# Production database (PostgreSQL/MySQL recommended)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # or mysql
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('RDS_PASSWORD'),
        'HOST': config('RDS_HOST'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# AWS S3 Configuration for Production
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

# Separate locations for media and static files in S3
AWS_LOCATION = 'media'
AWS_STATIC_LOCATION = 'static'

# Production Storage - Everything goes to S3
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "location": AWS_LOCATION,
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
        "OPTIONS": {
            "location": AWS_STATIC_LOCATION,
        },
    },
}

# Production URLs for static and media files
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_STATIC_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'

# Security settings for production
# SECURE_SSL_REDIRECT = True
# SECURE_HSTS_SECONDS = 31536000  # 1 year
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_BROWSER_XSS_FILTER = True
# X_FRAME_OPTIONS = 'DENY'
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Session security
# SESSION_COOKIE_SECURE = True
# SESSION_COOKIE_HTTPONLY = True
# CSRF_COOKIE_SECURE = True
# CSRF_COOKIE_HTTPONLY = True

# Production email settings
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = config('EMAIL_HOST', default='smtp.gmail.com')
# EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='abc@gmail.com')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='1')

# Production logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'django.log',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['file', 'console'],
        'level': 'INFO',
    },
}

print("🚀 Running in PRODUCTION mode")