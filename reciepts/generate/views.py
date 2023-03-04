from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Reciepts
from django.urls import reverse

# Create your views here.


def home(request):
    if request.method == 'GET':
        return render(request, 'generate/home.html')
    else:
        if request.method == 'POST':
            data = Reciepts()
            data.amount = request.POST['amount']
            data.name_student = request.POST['name_student']
            data.name_Payer = request.POST['name_Payer']
            data.description = request.POST['description']
            data.balance = request.POST['balance']
            data.save()
            return HttpResponseRedirect(reverse('reciepts:reciept', args=(data.pk,)))


def reciepts(request, num):
    data = Reciepts.objects.get(pk=num)
    context = {'Reciepts': data}
    return render(request, 'generate/reciepts.html', context)

def getRecentList(request):
    """

    :param request: httprequest
    :return: a list of all the reciepts that have been issued
    """
    data = Reciepts.objects.all()
    context = {'list_of_receipts': data}
    return render(request, 'generate/blah.html', context)


def get_by_name(request, name_of_student):

    #filter function needs to be fixed
    data = Reciepts.objects.filter('blah')
    context = {'list_of_receipts': data}
    return render(request, 'generate/blah.html', context)