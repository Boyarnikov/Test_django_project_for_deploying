from django.http import HttpResponse


def index(request):
    return HttpResponse("<H1>Index page</H1>")
