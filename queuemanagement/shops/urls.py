from django.urls import path
from . import views

app_name = 'shops'

urlpatterns = [
    path('', views.shops_list, name="Shops"),
]