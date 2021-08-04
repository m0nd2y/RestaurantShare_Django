from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *

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

def Create_category(request) :
    category_name = request.POST['categoryName']
    new_category = Category(category_name = category_name)
    new_category.save()
    return HttpResponseRedirect(reverse('index'))
    #return HttpResponse("여기서 category Create 기능을 구현할 예정")