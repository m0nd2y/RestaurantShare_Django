from django.http.response import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
def sendEmail(requests) :
    return HttpResponse("sendEmail")