import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Item
# Create your views here.

def home(request):
    shirt_list = Item.objects.filter(Shirt = True)[:7]
    jumper_list = Item.objects.filter(Jumper_Jacket=True)[:7]
    pants_list = Item.objects.filter(Pants=True)[:7]
    shoes_list = Item.objects.filter(Shoes=True)[:7]
    context = { 'shirt_list':shirt_list, 'jumper_list':jumper_list, 'pants_list':pants_list, 'shoes_list':shoes_list}
    return render(request, 'base/home.html', context)

def item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {'item': item}
    return render(request, 'base/item.html', context)

def catagory(request,catagory):

    item_list = Item.objects.order_by('created')

    sort_value = 'Newest-Release'

    if 'sort_value' in request.GET:
        if (request.GET['sort_value'] == 'Oldest-Release'):
            item_list = Item.objects.order_by('-created')
            sort_value = 'Oldest-Release'
        elif (request.GET['sort_value'] == 'Price-low-to-high'):
            item_list = Item.objects.order_by('Price')
            sort_value = 'Price-low-to-high'
        elif (request.GET['sort_value'] == 'Price-high-to-low'):
            item_list = Item.objects.order_by('-Price')
            sort_value = 'Price-high-to-low'
        else:
            item_list = Item.objects.order_by('created')
            sort_value = 'Newest-Release'

    if (catagory == 'Shirts'):
        item_list = item_list.filter(Shirt = True)
    elif(catagory == 'Jumpers'):
        item_list = item_list.filter(Jumper_Jacket=True)
    elif (catagory == 'Pants'):
        item_list = item_list.filter(Pants=True)
    elif (catagory == 'Shoes'):
        item_list = item_list.filter(Shoes=True)
    else:
        return redirect('home')

    context = {'catagory': catagory, 'item_list': item_list, 'sort_value': sort_value}
    return render(request, 'base/catagory.html', context)
