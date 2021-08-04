from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *

# Create your views here.
def index(request) :
    #return HttpResponse("inedx")
    categories = Category.objects.all()
    content = {'categories':categories}
    return render(request, 'ShareRes/index.html', content)

def restaurantDetail(request) :
    #return HttpResponse("restaurantDetail")
    return render(request, 'ShareRes/restaurantDetail.html')
    
def restaurantCreate(request) :
    #return HttpResponse("restaurantCreate")
    return render(request, 'ShareRes/restaurantCreate.html')
    
def categoryCreate(request) :
    categories = Category.objects.all()
    content = {'categories':categories}
    #return HttpResponse("categoryCreate")
    return render(request, 'ShareRes/categoryCreate.html', content)

def Create_category(request) :
    category_name = request.POST['categoryName']
    new_category = Category(category_name = category_name)
    new_category.save()
    return HttpResponseRedirect(reverse('index'))
    #return HttpResponse("여기서 category Create 기능을 구현할 예정")

def Delete_category(request) :
    category_id = int(request.POST['categoryId'].split("/")[0])
    delete_category = Category.objects.get(id = category_id)
    delete_category.delete()
    return HttpResponseRedirect(reverse('cateCreatePage'))