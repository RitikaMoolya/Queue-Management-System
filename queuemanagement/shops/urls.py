from django.urls import path

from . import views

app_name = 'shops'

urlpatterns = [
    path('', views.shops_list, name="Shops"),
    path('dashboard/', views.dashboard, name="Dashboard"),
    path('new-shop/', views.shop_new, name="New-Shop"),
    path('<int:pk>', views.shop_profile, name="Profile"),
    path('book_appointment/<int:pk>', views.book_appointment, name="book_appointment"),
]