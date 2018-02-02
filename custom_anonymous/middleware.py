import importlib
from django.conf import settings
from django.utils.functional import SimpleLazyObject
from django.contrib.auth import get_user
from django.contrib.auth.middleware import AuthenticationMiddleware as DjangoAuthenticationMiddleware

module, klass = settings.AUTH_ANONYMOUS_MODEL.rsplit('.', 1)
AnonymousUser = getattr(importlib.import_module(module), klass)


def get_cached_user(request):
    if not hasattr(request, '_cached_user'):
        user = get_user(request)
        if user.is_anonymous:
            user = AnonymousUser(request)

        request._cached_user = user

    return request._cached_user


class AuthenticationMiddleware(DjangoAuthenticationMiddleware):
    def process_request(self, request):
        assert hasattr(request, 'session'), (
            "The Django authentication middleware requires session middleware "
            "to be installed. Edit your MIDDLEWARE_CLASSES setting to insert "
            "'django.contrib.sessions.middleware.SessionMiddleware' before "
            "'account.middleware.AuthenticationMiddleware'."
        )
        request.user = SimpleLazyObject(lambda: get_cached_user(request))

