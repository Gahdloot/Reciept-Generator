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
            data.save()
            return HttpResponseRedirect(reverse('reciepts:reciept', args=(data.pk,)))


def reciepts(request, num):
    data = Reciepts.objects.get(pk=num)
    context = {'Reciepts': data}
    return render(request, 'generate/reciepts.html', context)
