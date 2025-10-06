from django.db.models.fields import return_None
from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import Books

def books(request):
    allbooks = Books.objects.all().values()
    template = loader.get_template('AllBooks.html')
    context = {
        'AllBooks': allbooks,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    book = Books.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'Book' : book
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
