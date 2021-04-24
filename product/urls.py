from django.urls import path
from product.views import *

urlpatterns = [
    path(
        'get-product-list',
        GetAllProducts.as_view(),
        name="Get All Products"
    ),
    path(
        'modify-product',
        ManageProducts.as_view(),
        name="Modify Products"
    ),
    path(
        'remove-product/<item_id>',
        RemoveProducts.as_view(),
        name="Remove Products"
    )
]