from django.urls import path

from .views import *

urlpatterns = [
    path("admin/sign-up", AdministratorAPIView.as_view(), name="admin-sign-up"),
    path(
        "store-owner/sign-up", StoreOwnerAPIView.as_view(), name="store-owner-sign-up"
    ),
    path(
        "store-manager/sign-up", StoreManagerAPIView.as_view(), name="store-manager-up"
    ),
    path("producer/sign-up", ProducerAPIView.as_view(), name="producer-sign-up"),
    path(
        "product-category",
        ProductCategoryListCreateAPIView.as_view(),
        name="product-category-list-create",
    ),
    path(
        "product-type",
        ProductTypeListCreateAPIView.as_view(),
        name="product-type-list-create",
    ),
    path("product", ProductListCreateAPIView.as_view(), name="product-create"),
    path(
        "product-category/<int:pk>/",
        ProductCategoryUpdateDeleteAPIView.as_view(),
        name="product-category-list-create",
    ),
    path(
        "product-type/<int:pk>/",
        ProductTypeUpdateDeleteAPIView.as_view(),
        name="product-type-list-create",
    ),
    path(
        "product/<int:pk>/", ProductUpdateDeleteAPIView.as_view(), name="product-create"
    ),
]
