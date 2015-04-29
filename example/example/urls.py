from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'example.views.test', name='test'),
)

