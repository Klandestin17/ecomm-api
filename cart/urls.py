from django.urls import path
from cart import views

urlpatterns = [
    path("me/", views.GetUserCart.as_view(), name="get-useer-cart"),
    path("add/", views.AddItemTocart.as_view(), name="add-to-cart"),
    path("count/", views.CartCount.as_view(), name="count"),
    path("delete/", views.RemoveItemFromCart.as_view(), name="delete"),
    path("update/", views.UpdateCartItemQuantity.as_view(), name="update"),
]
