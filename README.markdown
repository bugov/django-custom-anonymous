# django-custom-anonymous


[![Build Status](https://travis-ci.org/bugov/django-custom-anonymous.svg?branch=master)](https://travis-ci.org/bugov/django-custom-anonymous)

Library provides customization of AnonymousUser.

Works with Python >= 2.6, >= 3.2, Django >= 1.5, >= 2.0.

## Installation

    pip install django-custom-anonymous

## Customization

Add to `settings`:

    AUTH_ANONYMOUS_MODEL = 'your_app.module.CustomAnonymousUser'

Add to middlewares:

    MIDDLEWARE = (
    ...
        'custom_anonymous.middleware.AuthenticationMiddleware',
    ...
    )

Create your own anonymous (for example):

    from django.contrib.auth.models import AnonymousUser as DjangoAnonymousUser
    ...
    class CustomAnonymousUser(DjangoAnonymousUser):
        ip = None

        def __init__(self, request):
            self.ip = request.META.get('REMOTE_ADDR')
            super(AnonymousUser, self).__init__()
