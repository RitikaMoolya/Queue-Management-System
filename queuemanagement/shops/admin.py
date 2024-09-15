from django.contrib import admin
from .models import Shop
from .models import Token
from .models import Category

# Register your models here.
admin.site.register(Shop)
admin.site.register(Token)
admin.site.register(Category)