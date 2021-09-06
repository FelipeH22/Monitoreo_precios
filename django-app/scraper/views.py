#scrapper libaris
import requests
from bs4 import BeautifulSoup

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse

#scrapper functions
get_precio=lambda codigo: str(codigo.find('div', class_='product-info--price-new')).split("\n")[1].rsplit("<")[0].strip()[1:]
get_nombre=lambda url: " ".join(url.split(".com/")[1].split("-"))
get_producto=lambda url: get_precio(BeautifulSoup(requests.get(url).content, 'html.parser'))
get_tienda=lambda url: url.split(".com/")[0].split(".")[1]

#import pdb

# Create your views here.

def scraper(request,email):
    #return HttpResponse(str(posts))    

    #pdb.set_trace()
    email = email

    if request.method=='POST':

        url = request.POST['url_product']

        context = {
            'email':email
        }

        if len(url) < 20:
            context['error']='Link luce erroneó'
            return render(request,'new.html',context)
        else:
            tienda = get_tienda(url)
            context['tienda']=tienda
            return render(request,'new.html',context)    

    context = {
        'email':email
    }

    return render(request,'new.html',context)
