from django import forms 
from . import models 

class CreateShop(forms.ModelForm): 
    class Meta: 
        model = models.Shop
        fields = ['name','bio','contact','address','timings','image','category']