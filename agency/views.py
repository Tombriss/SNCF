from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the agency index.")

def homepage(request):
    return render(request, 'homepage.html')

def ridesearch(request):
    return render(request, 'ridesearch.html')

def availability(request):
    return render(request, 'availability.html')

def confirmation(request):
    return render(request, 'confirmation.html')

def ticket(request):
    return render(request, 'ticket.html')