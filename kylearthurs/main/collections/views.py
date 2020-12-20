from django.http import HttpResponse
from django.template import loader
from main.models import Book, Record, Game, System


def collections(request):
    template = loader.get_template('main/collections.html')
    context = {}
    return HttpResponse(template.render(context, request))

def books(request):
    template = loader.get_template('main/collections/books.html')
    import pdb; pdb.set_trace()
    context = {}
    return HttpResponse(template.render(context, request))

def records(request):
    template = loader.get_template('main/collections/records.html')
    context = {}
    return HttpResponse(template.render(context, request))

def games(request):
    template = loader.get_template('main/collections/games.html')
    context = {}
    return HttpResponse(template.render(context, request))