import calendar

from product.models import Productos
from django.shortcuts import render
from django.http import HttpResponse, request

import pdb;

#Models
from user.models import precios_productos_cliente as ppc
from product.models import Precios_producto as pp

# Create your views here.
def show_products(request,email):

    email = email
    list_precios = ppc.objects.filter(correo=email)

    productos = {}

    for i in list_precios:
        productos[i.nombre] = i.precio

    productos = productos.items()
    context = {'email': email, 'productos':productos}
    #pdb.set_trace()
    return render(request,'my_products.html',context)


def show_details(request,name_product):


    email = 'dasdadas'
    name_product = name_product

    list_precios = pp.objects.filter(nombre=name_product)


    precios = []
    labels = []

    for i in list_precios:
        precios.append(i.precio)
        labels.append(calendar.month_name[i.fecha.month])
    
    store = list_precios.first().tienda
    link = list_precios.first().url
    precio_mas_bajo = min(precios)
    
    #pdb.set_trace()

    context = {
        'email': email,
        'name_product':name_product,
        'precios':precios,
        'labels':labels,
        'store':store,
        'link':link,
        'precio_mas_bajo':precio_mas_bajo
        }

    return render(request,'detail_product.html',context) 
    

