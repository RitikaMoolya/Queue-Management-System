from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    category_title = models.CharField(max_length=20)

    def __str__(self):
            return self.category_title

class Shop(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shops")
    name = models.CharField(max_length=75)
    bio = models.TextField()
    contact = models.CharField(max_length=15)
    address = models.TextField()
    timings = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")

    def __str__(self):
        return self.name
        

class Token(models.Model):
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    number = models.IntegerField()
    current = models.BooleanField()


