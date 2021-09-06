from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

#Exception
from django.core.exceptions import ObjectDoesNotExist

#Models
from user.models import Personas

# Create your views here.
def log(request):
    #import pdb
    #pdb.set_trace()

    if request.method == 'POST':

        user = request.POST['email']
        passoword  =  request.POST['pass']
        email = user

        context = {
                'email': email
        }

        try:
            m = Personas.objects.get(email=user)
        except ObjectDoesNotExist:
            return render(request,'login.html',{'error':"Your email is not exist."})

        if m.password == passoword:

            request.session['member_id'] = m.id
            #return HttpResponse("You're logged in.")
            return HttpResponseRedirect(reverse('products', args=(user,)))

            return render(request,'my_products.html',context)
        else:
            context['error'] = "Your username and password didn't match."
            return render(request,'login.html',context)

        """m = Member.objects.get(username=request.POST['username'])
        """
    context = {
        'email': None
    }

    return render(request,'login.html')

    