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

def business_finance(request):
    template = loader.get_template('main/business-finance.html')
    context = {}
    return HttpResponse(template.render(context, request))

def philosophy_philanthropy(request):
    template = loader.get_template('main/philosophy-philanthropy.html')
    context = {}
    return HttpResponse(template.render(context, request))

def collections(request):
    template = loader.get_template('main/collections.html')
    context = {}
    return HttpResponse(template.render(context, request))
