from django import forms 
from . import models 

class CreateShop(forms.ModelForm): 
    class Meta: 
        model = models.Shop
        fields = ['name','category','bio','contact','address','timings','image','upload_promotional_images_1','upload_promotional_images_2','upload_promotional_images_3','upload_promotional_images_4']