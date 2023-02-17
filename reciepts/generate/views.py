from django.shortcuts import render, redirect
from .models import Reciepts

# Create your views here.


def home(request):

    return render(request, 'reciepts/home.html')


def reciepts(request):



    context = {}
    if request.method == 'POST':
        data = Reciepts()
        data.amount = request.data['amount']
        data.name_student = request.data['name_student']
        data.name_Payer = request.data['name_Payer']
        data.description = request.data['description']



    return render(request, 'reciepts/home.html')