from django.urls import path

from .views import *

urlpatterns = [
    path("api/admin/sign-up", AdministratorAPIView.as_view(), name="admin-sign-up"),
    path(
        "api/store-owner/sign-up", StoreOwnerAPIView.as_view(), name="store-owner-sign-up"
    ),
    path(
        "api/store-manager/sign-up", StoreManagerAPIView.as_view(), name="store-manager-up"
    ),
    path("api/producer/sign-up", ProducerAPIView.as_view(), name="producer-sign-up"),
    path(
        "api/product-category",
        ProductCategoryListCreateAPIView.as_view(),
        name="product-category-list-create",
    ),
    path(
        "api/product-type",
        ProductTypeListCreateAPIView.as_view(),
        name="product-type-list-create",
    ),
    path("api/product", ProductListCreateAPIView.as_view(), name="product-create"),
    path(
        "api/product-category/<int:pk>/",
        ProductCategoryUpdateDeleteAPIView.as_view(),
        name="product-category-list-create",
    ),
    path(
        "api/product-type/<int:pk>/",
        ProductTypeUpdateDeleteAPIView.as_view(),
        name="product-type-list-create",
    ),
    path(
        "api/product/<int:pk>/", ProductUpdateDeleteAPIView.as_view(), name="product-create"
    ),
]
