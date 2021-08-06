from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def sendEmail(requests) :
    return HttpResponseRedirect(reverse('index'))
    #return HttpResponse("sendEmail")
