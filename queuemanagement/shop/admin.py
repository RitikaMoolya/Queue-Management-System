from django.contrib import admin
from .models import Shop
from .models import Token

# Register your models here.
admin.site.register(Shop)
admin.site.register(Token)