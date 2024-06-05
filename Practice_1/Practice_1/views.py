from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')
    #return HttpResponse("Hello World!")

def about(request):
    return HttpResponse("About Page!")

def index(request):
    return render(request,'index.html')