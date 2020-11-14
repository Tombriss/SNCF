from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the agency index.")

def homepage(request):
    return render(request, 'agency/homepage.html')



def newclient(request):
    return render(request, 'agency/newclient.html')

def nc_ridesearch(request):
    return render(request, 'agency/nc_ridesearch.html')

def nc_availablerides(request):
    return render(request, 'agency/nc_availablerides.html')

def nc_ticket(request):
    return render(request, 'agency/nc_ticket.html')



def existingclient(request):
    return render(request, 'agency/existingclient.html')

def ec_ridesearch(request):
    return render(request, 'agency/ec_ridesearch.html')

def ec_availablerides(request):
    return render(request, 'agency/ec_availablerides.html')

def ec_ticket(request):
    return render(request, 'agency/ec_ticket.html')




def bookedrides(request):
    return render(request, 'agency/bookedrides.html')

def listofrides(request):
    return render(request, 'agency/listofrides.html')
