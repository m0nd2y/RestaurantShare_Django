from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request) :
    #return HttpResponse("inedx")
    return render(request, 'ShareRes/index.html')

def restaurantDetail(request) :
    #return HttpResponse("restaurantDetail")
    return render(request, 'ShareRes/restaurantDetail.html')
    
def restaurantCreate(request) :
    #return HttpResponse("restaurantCreate")
    return render(request, 'ShareRes/restaurantCreate.html')
    
def categoryCreate(request) :
    #return HttpResponse("categoryCreate")
    return render(request, 'ShareRes/categoryCreate.html')