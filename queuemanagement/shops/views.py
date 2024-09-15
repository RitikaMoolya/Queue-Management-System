from django.shortcuts import render,redirect
from .models import Shop
from . import forms 

# Create your views here.

def shops_list(request):
    shops = Shop.objects.all()
    return render(request, 'shops/shops_list.html', {'shops': shops})

def shop_profile(request,pk):
    shop = Shop.objects.get(pk=pk)
    return render(request, 'shops/shop_profile.html', {'shop': shop})

def shop_new(request):
    if request.method == 'POST': 
        form = forms.CreateShop(request.POST, request.FILES) 
        if form.is_valid():
            newshop = form.save(commit=False) 
            newshop.owner = request.user 
            newshop.save()
            return redirect('shops:Shops')
    else:
        form = forms.CreateShop()
    return render(request, 'shops/shop_new.html', { 'form': form })

