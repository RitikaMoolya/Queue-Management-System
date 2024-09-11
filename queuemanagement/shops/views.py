from django.shortcuts import render,redirect
from .models import Shop

# Create your views here.

def shops_list(request):
    shops = Shop.objects.all()
    return render(request, 'shops/shops_list.html', {'shops': shops})
