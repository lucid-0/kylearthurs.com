from django.http import HttpResponse
from django.template import loader

def collections(request):
    template = loader.get_template('main/collections.html')
    context = {}
    return HttpResponse(template.render(context, request))