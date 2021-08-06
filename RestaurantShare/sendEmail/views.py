from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from ShareRes.models import *


# Create your views here.
def sendEmail(requests) :
    checked_res_list = requests.POST.getlist('checks')
    inputReceiver = requests.POST['inputReceiver']
    inputTitle = requests.POST['inputTitle']
    inputContent = requests.POST['inputContent']
    mail_html = "<html><body>"
    mail_html += "<h1> 맛집 공유 </h1>"
    mail_html += "<p>"+inputContent+"<br>"
    mail_html += "발신자님께서 공유하신 맛집은 다음과 같습니다.</p>"
    for checked_res_id in checked_res_list :
        restaurant = Restaurant.objects.get(id=checked_res_id)
        mail_html += "<h2>" + restaurant.restaurant_name+"</h3>"
        mail_html += "<h4>* 관련 링크</h4>"+"<p>"+ restaurant.restaurant_link+"</p><br>"
        mail_html += "<h4>* 상세 내용</h4>"+"<p>"+ restaurant.restaurant_content+"</p><br>"
        mail_html += "<h4>* 관련 키워드</h4>"+"<p>"+ restaurant.restaurant_keyword+"</p><br>"
        mail_html += "<br>"
    mail_html += "</body></html>"
    print(mail_html)
    return HttpResponseRedirect(reverse('index'))
    #return HttpResponse("sendEmail")
