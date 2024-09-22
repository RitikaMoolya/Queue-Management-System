from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    category_title = models.CharField(max_length=20)

    def __str__(self):
        return self.category_title


class Shop(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shops')
    name = models.CharField(max_length=75)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    bio = models.TextField()
    contact = models.CharField(max_length=15)
    address = models.TextField()
    timings = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True)
    upload_promotional_images_1=models.ImageField(upload_to="images/", null=True)
    upload_promotional_images_2=models.ImageField(upload_to="images/", null=True)
    upload_promotional_images_3=models.ImageField(upload_to="images/", null=True)
    upload_promotional_images_4=models.ImageField(upload_to="images/", null=True)
    

    def __str__(self):
        return self.name


class Token(models.Model):
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    number = models.IntegerField()
    current = models.BooleanField()