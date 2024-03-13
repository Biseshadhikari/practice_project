from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home(request):
    # return HttpResponse('Home Page')
    return render(request,'base.html')

def about_us(request):
    # return HttpResponse('<h1 style = "color:red">hello world</h1>')
    
    context = { 
        'name':"bisesh adhikari",
        "address":"biratnagar",
        "phones":['9812356379','984524544040']
    }
    return render(request,'app/about.html',context)





