from django.http import HttpResponse
from django.shortcuts import render
from data.models import *

def get_item(request, item_id):
    context = {'item' : Item.objects.get(id=item_id)}
    return render(request, 'data/item.html', context)