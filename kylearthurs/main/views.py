from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('main/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def dev(request):
    template = loader.get_template('main/dev.html')
    context = {}
    return HttpResponse(template.render(context, request))
    return 