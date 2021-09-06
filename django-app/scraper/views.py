#scrapper libraris
import requests
from bs4 import BeautifulSoup

#import django 
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse

#import models 
from product.models import Productos

#scrapper functions
get_precio=lambda codigo: str(codigo.find('div', class_='product-info--price-new')).split("\n")[1].rsplit("<")[0].strip()[1:]
get_nombre=lambda url: " ".join(url.split(".com/")[1].split("-"))
get_producto=lambda url: get_precio(BeautifulSoup(requests.get(url).content, 'html.parser'))
get_tienda=lambda url: url.split(".com/")[0].split(".")[1]

#debbuger
import pdb


#variables 
upload = False
tienda = ''
nombre = ''
producto = ''
link = ''

# Create your views here.
def scraper(request,email):
    #return HttpResponse(str(posts))    
    #pdb.set_trace()
    email = email

    global upload
    global tienda
    global link
    global nombre
    global producto

    if request.method == 'POST' and upload:

        context={}
        context['tienda']=tienda
        context['nombre']=nombre
        context['producto']=producto
        context['email'] = email
        context['link'] = link
        saved = 'Guardado!'
        context['saved'] = saved

        p = Productos(nombre= nombre,tienda=tienda,url=link)
        p.save()

        upload = False
        return render(request,'new.html',context)

    elif request.method=='POST':
        url = request.POST['url_product']

        context = {
            'email':email
        }

        if len(url) < 20:
            context['error']='Link luce erroneó'
            return render(request,'new.html',context)
        else:

            tienda_got = get_tienda(url)
            nombre_got = get_nombre(url)
            producto_got = get_producto(url)

            context['tienda']=tienda_got
            context['nombre']=nombre_got
            context['producto']=producto_got
            
            tienda=tienda_got
            nombre=nombre_got
            producto=producto_got
            link = url
            upload = True
            url = None
            return render(request,'new.html',context)    

    context = {
        'email':email
    }

    return render(request,'new.html',context)
