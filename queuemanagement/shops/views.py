from datetime import date
from django.shortcuts import render,redirect
from .models import Shop, Token, Category
from . import forms 
from django.db.models import Max

# Create your views here.

def shops_list(request):
    category = request.GET.get('category')
    shops = Shop.objects.all()
    if category:
        category = int(category)
        shops = shops.filter(category = category)
    categories = Category.objects.all()
    return render(request, 'shops/shops_list.html', {'shops': shops, 'categories': categories, 'category':category})

def shop_profile(request,pk):
    shop = Shop.objects.get(pk=pk)
    current = shop.token_set.filter(current = True, date = date.today()).first()
    next_number = shop.token_set.filter(date = date.today()).aggregate(Max('number', default = 0))
    next_number = next_number['number__max'] + 1
    return render(request, 'shops/shop_profile.html', {'shop': shop, 'current' : current, 'number': next_number})

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


    
    
