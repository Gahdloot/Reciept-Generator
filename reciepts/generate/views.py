from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Reciepts
from django.urls import reverse

# Create your views here.


def home(request):
    if request.method == 'GET':
        return render(request, 'reciepts/home.html')
    else:
        if request.method == 'POST':
            data = Reciepts()
            data.amount = request.data['amount']
            data.name_student = request.data['name_student']
            data.name_Payer = request.data['name_Payer']
            data.description = request.data['description']
            data.save()
            return HttpResponseRedirect(reverse('reciepts:reciept', args=(data.reciept_number,)))


def reciepts(request, reciept):
    data = Reciepts.objects.get(reciept_number=reciept)
    context = {'Reciepts': data}
    return render(request, 'reciepts/home.html', context)
