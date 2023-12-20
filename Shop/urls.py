from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [ 
    path('',index, name='index'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('product/create/', product_create, name='product_create'),
    #Shopping Carts URLs
    path('cart/', cart_detail , name='cart-detail'),
    path('cart/add/<int:pk>/', cart_add, name='cart-add'),
    path('cart/remove/<int:pk>/', cart_remove, name='cart-remove'),
    path('cart/update/<int:pk>/', cart_update, name='cart-update'),
]
