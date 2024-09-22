from datetime import date

from django.contrib.auth.decorators import login_required
from django.db.models import Max
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


@login_required
def dashboard(request):
    user_tokens = Token.objects.filter(date=date.today(), user=request.user).prefetch_related('shop')
    current_tokens = []
    for user_token in user_tokens:
        current_tokens.append(Token.objects.filter(shop=user_token.shop, date=date.today(), current=True).first())
    tokens = list(zip(user_tokens, current_tokens))
    shops = Shop.objects.filter(owner=request.user)
    shops_data = []
    for shop in shops:
        shop_tokens = Token.objects.filter(shop=shop, date=date.today()).prefetch_related('user')
        total_bookings = shop_tokens.count()
        current_token = Token.objects.filter(shop=shop, date=date.today(), current=True).first()
        shops_data.append({
            'current': current_token,
            'total': total_bookings,
            'shop_tokens': shop_tokens,
            'shop_name': shop.name,
        })
    return render(request, 'shops/dashboard.html', {'tokens': tokens, 'shops_data': shops_data})


@login_required
@require_http_methods(['POST'])
def book_appointment(request, pk):
    shop = Shop.objects.get(pk=pk)
    next_number = shop.token_set.filter(date=date.today()).aggregate(Max('number', default=0))['number__max'] + 1
    Token.objects.get_or_create(
        user=request.user, shop=shop, date=date.today(), defaults={'number': next_number, 'current': False}
    )
    return redirect('shops:Profile', pk=pk)