from datetime import date

from django.contrib.auth.decorators import login_required
from django.db.models import F, Max
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from . import forms
from .models import Category, Shop, Token

# Create your views here.


def shops_list(request):
    category = request.GET.get('category')
    shops = Shop.objects.all()
    if category:
        category = int(category)
        shops = shops.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'shops/shops_list.html', {'shops': shops, 'categories': categories, 'category': category})


def shop_profile(request, pk):
    shop = Shop.objects.get(pk=pk)
    current = shop.token_set.filter(current=True, date=date.today()).first()
    your_num = shop.token_set.filter(date=date.today(), user=request.user).first()
    next_number = shop.token_set.filter(date=date.today()).aggregate(Max('number', default=0))['number__max'] + 1
    if your_num:
        your_num = your_num.number
    return render(
        request,
        'shops/shop_profile.html',
        {
            'shop': shop,
            'current': current,
            'next_number': next_number,
            'your_num': your_num,
        },
    )


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
    return render(request, 'shops/shop_new.html', {'form': form})


def dashboard(request):
    return render(request, 'shops/dashboard.html')


@login_required
@require_http_methods(['POST'])
def book_appointment(request, pk):
    shop = Shop.objects.get(pk=pk)
    next_number = shop.token_set.filter(date=date.today()).aggregate(Max('number', default=0))['number__max'] + 1
    Token.objects.get_or_create(
        user=request.user, shop=shop, date=date.today(), defaults={'number': next_number, 'current': False}
    )
    return redirect('shops:Profile', pk=pk)
