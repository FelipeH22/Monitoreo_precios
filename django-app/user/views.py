from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def log(request):
    #import pdb
    #pdb.set_trace()
    if request.method == 'POST':
        print('*'*10)
        user = request.POST['user']
        print('*'*10)
    return render(request,'login.html')
