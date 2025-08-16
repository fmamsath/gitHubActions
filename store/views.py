from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, "store/home.html", {"products": products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "store/product_detail.html", {"product": product})

def cart_detail(request):
    cart = request.session.get(settings.CART_SESSION_ID, {})
    total = sum(item["price"] * item["qty"] for item in cart.values())
    return render(request, "store/cart.html", {"cart": cart, "total": total})

def cart_add(request, slug):
    product = get_object_or_404(Product, slug=slug)
    try:
        qty = int(request.POST.get('quantity', 1))
        if qty < 1:
            qty = 1
    except ValueError:
        qty = 1

    cart = request.session.get(settings.CART_SESSION_ID, {})
    item = cart.get(slug, {"name": product.name, "price": float(product.price), "qty": 0})
    item["qty"] += qty
    cart[slug] = item
    request.session[settings.CART_SESSION_ID] = cart

    return redirect("store:cart_detail")


def cart_remove(request, slug):
    cart = request.session.get(settings.CART_SESSION_ID, {})
    if slug in cart: del cart[slug]
    request.session[settings.CART_SESSION_ID] = cart
    return redirect("store:cart_detail")
