from django.urls import path
from .views import *


urlpatterns=[
    path("add-cart-item/<int:cartitem_id>/", add_cart_item, name="add-cart-item"),
    path("subtract-cart-item/<int:cartitem_id>/",subtract_cart_item, name="subtract-cart-item"),
    path("remove-cart-item/<int:cartitem_id>/",remove_cart_item, name="remove-cart-item"),
    path("cart/", cart, name="cart"),
    path("cart_copy/<str:message>/", cart_copy, name="cart-copy"),
    path("cart/add-to-cart/", add_to_cart, name="add_to_cart"),
    path("wishlist/<int:pk>/<str:data>/", add_to_wishlist, name="add-to-wishlist"),
    path("wishlist/", wishlist_items, name="wishlist"),
    path("remove-wishlist/<int:pk>/<str:data>/", remove_wishlist, name="remove-wishlist"),
]