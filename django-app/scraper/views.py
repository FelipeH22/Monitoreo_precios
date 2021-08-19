from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def scraper(request):
    #posts = [1,2,3]
    #return HttpResponse(str(posts))
    return render(request,'new.html')
