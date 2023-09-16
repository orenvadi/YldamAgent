from rest_framework import generics

from .models import *
from .serializers import *


class AdministratorAPIView(generics.CreateAPIView):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer


class StoreOwnerAPIView(generics.ListCreateAPIView):
    queryset = StoreOwner.objects.all()
    serializer_class = StoreOwnerSerializer


class StoreManagerAPIView(generics.ListCreateAPIView):
    queryset = StoreManager.objects.all()
    serializer_class = StoreManagerSerializer


class ProducerAPIView(generics.ListCreateAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer


class ProductCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductTypeListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCategoryUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductTypeUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class ProductUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
