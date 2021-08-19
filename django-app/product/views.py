from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def show_products(request):
    return render(request,'my_products.html')

def show_details(request):
    return render(request,'detail_product.html')
