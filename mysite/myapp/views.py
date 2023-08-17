from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from .models import Link
from django.views import View
from rest_framework import viewsets
from .serializers import LinkSerializer


# Create your views here.

class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()


# def scrape(request):
#     if request.method == "POST":
#         site = request.POST.get('site','')
#         page = requests.get(site)
#         soup = BeautifulSoup(page.text,'html.parser')

    
#         for link in soup.find_all('a'):
#             link_address = link.get('href')
#             link_text = link.string
#             Link.objects.create(address=link_address,name=link_text)
#         return HttpResponseRedirect('/')
#     else:
#         data = Link.objects.all()

#     return render(request,'myapp/result.html',{'data':data})

class ScrapeView(View):
    template_name = 'myapp/result.html'

    def get(self, request, *args, **kwargs):
        data = Link.objects.all()
        return render(request, self.template_name, {'data': data})

    def post(self, request, *args, **kwargs):
        site = request.POST.get('site', '')
        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')

        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            Link.objects.create(address=link_address, name=link_text)
        return HttpResponseRedirect('/')


# def clear(request):
#     Link.objects.all().delete()
#     return render(request,'myapp/result.html')

class ClearView(View):
    template_name = 'myapp/result.html'

    def get(self, request, *args, **kwargs):
        Link.objects.all().delete()
        return render(request, self.template_name)

