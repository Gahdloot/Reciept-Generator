from django.urls import path

from . import views

app_name = 'reciepts'
urlpatterns = [
    path('', views.home, name='home'),
    path('Chapelville/<int:num>', views.reciepts, name='reciept'),
]