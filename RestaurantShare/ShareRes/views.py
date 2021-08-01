from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request) :
    return HttpResponse("inedx")

def restaurentDetail(request) :
    return HttpResponse("restaurentDetail")
    
def restaurentCreate(request) :
    return HttpResponse("restaurentCreate")
    
def categoryCreate(request) :
    return HttpResponse("categoryCreate")