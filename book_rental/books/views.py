from contextlib import nullcontext
from tempfile import template

from django.contrib.admin.utils import lookup_spawns_duplicates
from django.db.models.fields import return_None
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from .models import Books



def books(request):
    allbooks = Books.objects.all().values()
    context = {
        'AllBooks': allbooks,
    }
    return render(request, 'AllBooks.html' ,context)

def details(request, id):
    book = Books.objects.get(id=id)
    context = {
        'Book' : book
    }
    return render(request,'details.html', context )

def newbook(request):
    if request.method =="POST":
        if request.POST.get("BookName") and request.POST.get("BookDescription"):
            BName, BDescription = request.POST.get("BookName"), request.POST.get("BookDescription")
            #print(request.POST.get("BookName"))
            #print(request.POST.get("BookDescription"))
            Books.objects.create(BookName=BName,BookDescription=BDescription)
    return render(request, 'NewBook.html')

# Create your views here.
def test(request):
    return render(request, 'TestTemplate.html')

def home(request):
    return render(request, 'Home.html')
