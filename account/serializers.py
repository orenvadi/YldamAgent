from rest_framework import serializers
from .models import *


class AdministratorSerializer(serializers.ModelSerializer):
    password_display = serializers.SerializerMethodField()

    def get_password_display(self, obj):
        return '*' * len(obj.password) if obj.password else ''

    class Meta:
        model = Administrator
        fields = "__all__"


class StoreOwnerSerializer(serializers.ModelSerializer):
    password_display = serializers.SerializerMethodField()

    def get_password_display(self, obj):
        return '*' * len(obj.password) if obj.password else ''

    class Meta:
        model = StoreOwner
        fields = "__all__"


class StoreManagerSerializer(serializers.ModelSerializer):
    password_display = serializers.SerializerMethodField()

    def get_password_display(self, obj):
        return '*' * len(obj.password) if obj.password else ''

    class Meta:
        model = StoreManager
        fields = "__all__"


class ProducerSerializer(serializers.ModelSerializer):
    password_display = serializers.SerializerMethodField()

    def get_password_display(self, obj):
        return '*' * len(obj.password) if obj.password else ''

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
