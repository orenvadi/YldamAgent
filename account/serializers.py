from rest_framework import serializers

from .models import *


class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = "__all__"


class StoreOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreOwner
        fields = "__all__"


class StoreManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreManager
        fields = "__all__"


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = "__all__"


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
