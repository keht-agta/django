import json
import shutil
from pprint import pprint

from django.http import HttpResponse
from django.shortcuts import render

from phone.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'name')
    if sort == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sort == 'price_low':
        phones = Phone.objects.all().order_by('price')
    elif sort == 'price_high':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all()
    context = {'phones': phones}
    print(sort)
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    print(type(phone))
    context = {'phone': phone}
    return render(request, template, context)




# Create your views here.
def index(request):
    url1, url2 = 'admin/' , 'catalog/'
    return HttpResponse(f'<a href={url1}> {url1}</a><br> <a href={url2}> {url2} </a>')
