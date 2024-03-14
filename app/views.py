from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.

def Home(request):
    properties = Property.objects.all()
    print(properties)
    context = {
        'properties':properties
    }
    return render(request,'base.html',context)

def about_us(request):


    context = { 
        'name':"bisesh adhikari",
        "address":"biratnagar",
        "phones":['9812356379','984524544040']
    }
    return render(request,'app/about.html',context)





