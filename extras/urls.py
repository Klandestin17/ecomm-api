from django.urls import path
from extras import views

urlpatterns = [
    path("addresslist/", views.GetUserAddress.as_view(), name="user-addresses"),
    path("add/", views.AddAddress.as_view(), name="add-addresses"),
    path("default/", views.SetDefaultAddress.as_view(), name="default-addresses"),
    path("delete/", views.DeleteAddress.as_view(), name="delete-addresses"),
    path("me/", views.GetDefaultAddress.as_view(), name="default-addresses"),
]
