from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path("", views.home, name="home"),
    path("product/<slug:slug>/", views.product_detail, name="product_detail"),
    path("cart/", views.cart_detail, name="cart_detail"),
    path("cart/add/<slug:slug>/", views.cart_add, name="cart_add"),
    path('cart/', views.cart_detail, name='cart_detail'),
    path("cart/remove/<slug:slug>/", views.cart_remove, name="cart_remove"),
]
