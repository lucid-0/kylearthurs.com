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

def philosophy(request):
    template = loader.get_template('main/philosophy.html')
    context = {}
    return HttpResponse(template.render(context, request))

def blog(request):
    template = loader.get_template('main/blog.html')
    context = {}
    return HttpResponse(template.render(context, request))