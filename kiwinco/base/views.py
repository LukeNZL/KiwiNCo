import os
from django.shortcuts import render
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def item(request):
    return render(request, 'base/item.html')

def catagory(request):
    return render(request, 'base/catagory.html')
