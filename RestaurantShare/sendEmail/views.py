from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def sendEmail(requests) :
    checked_res_list = requests.POST.getlist('checks')
    inputReceiver = requests.POST['inputReceiver']
    inputTitle = requests.POST['inputTitle']
    inputContent = request.POST['inputContent']
    print(checked_res_list,"/",inputReceiver,"/",inputTitle,"/",inputContent) 
    return HttpResponseRedirect(reverse('index'))
    #return HttpResponse("sendEmail")
