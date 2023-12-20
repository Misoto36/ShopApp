from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect

from .models import * 
from .utils import get_cart

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products' : products
    }
    return render(request, 'shop/index.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request,'shop/product_detail.html', context)

def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category = request.POST.get('category')
        category = Category.objects.get(id = category)
        product = Product.objects.create(
            name = name,
            description = description,
            price = price,
            category= category
        )
        return redirect('shop:product_detail', pk=product.id )
    context = {
        'categories':Category.objects.all()}
    return render(request, 'shop/product_create.html', context)



#Shopping Cart Views

def cart_detail(request):
    cart = get_cart(request)
    context = {
        'cart':cart
    }
    return render(request,'shop/detail.html', context)

def cart_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = get_cart(request)
    quantity = request.POST.get('quantity')
    cart_item, created = CartItem.objects.get_or_create(
        cart = cart,
        product = product,
        defaults={'quantity':quantity}
    )
    if not created:
        cart_item.quantity += int(quantity)
        cart_item.save()
    return redirect('shop:cart-detail')   

def cart_remove(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk)
    cart_item.delete()
    return redirect('shop:cart-detail')

def cart_update(request, pk):
    cart_item =  get_object_or_404(CartItem, pk = pk)
    quiantity = request.POST.get('quantity')
    cart_item.quantity = quiantity
    cart_item.save()
    return redirect('shop:cart-detail')
