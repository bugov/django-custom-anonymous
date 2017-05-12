from distutils.version import StrictVersion

import django
from django.conf.urls import url


if StrictVersion(django.get_version()) < StrictVersion('1.10'):
    from django.conf.urls import patterns

    urlpatterns = patterns('',
        url(r'^$', 'example.views.test', name='test'),
    )
else:
    from example.views import test

    urlpatterns = (
        url(r'^$', test, name='test'),
    )

