from django.http import HttpResponse


def test(request):
    return HttpResponse(content=request.user.sum(1, 2))

