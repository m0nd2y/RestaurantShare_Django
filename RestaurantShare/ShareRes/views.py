from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request) :
    return HttpResponse("inedx")

def restaurantDetail(request) :
    return HttpResponse("restaurantDetail")
    
def restaurantCreate(request) :
    return HttpResponse("restaurantCreate")
    
def categoryCreate(request) :
    return HttpResponse("categoryCreate")