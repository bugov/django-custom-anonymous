from django.contrib.auth.models import AnonymousUser as DjangoAnonymousUser


class AnonymousUser(DjangoAnonymousUser):
    def __init__(self, request):
        super(AnonymousUser, self).__init__()
    
    def sum(self, a, b):
        return a + b

