from rest_framework import serializers
from .models import *


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    # Create user
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class AdministratorSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(required=False)

    class Meta:
        model = Administrator
        fields = "__all__"


class StoreOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreOwner
        fields = "__all__"

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        email = user_data['email']
        password = user_data['password']

        user = CustomUser.objects.create_user(email=email, username=email)
        user.set_password(password)
        user.save()

        store_owner = StoreOwner.objects.create(user=user, **validated_data)
        return store_owner

    # Update data
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user_serializer = self.fields['user']
            user = instance.user
            user = user_serializer.update(user, user_data)
            validated_data['user'] = user
        return super().update(instance, validated_data)

    # Read data
    def retrieve(self, instance):
        user_serializer = self.fields['user']
        user_data = user_serializer.to_representation(instance.user)
        ret = super().retrieve(instance)
        ret.data['user'] = user_data
        return ret


class StoreManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreManager
        fields = "__all__"

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        email = user_data['email']
        password = user_data['password']

        user = CustomUser.objects.create_user(email=email, username=email)
        user.set_password(password)
        user.save()

        store_owner = StoreOwner.objects.create(user=user, **validated_data)
        return store_owner

    # Update data
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user_serializer = self.fields['user']
            user = instance.user
            user = user_serializer.update(user, user_data)
            validated_data['user'] = user
        return super().update(instance, validated_data)

    # Read data
    def retrieve(self, instance):
        user_serializer = self.fields['user']
        user_data = user_serializer.to_representation(instance.user)
        ret = super().retrieve(instance)
        ret.data['user'] = user_data
        return ret


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = "__all__"

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        email = user_data['email']
        password = user_data['password']

        user = CustomUser.objects.create_user(email=email, username=email)
        user.set_password(password)
        user.save()

        store_owner = StoreOwner.objects.create(user=user, **validated_data)
        return store_owner

    # Update data
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user_serializer = self.fields['user']
            user = instance.user
            user = user_serializer.update(user, user_data)
            validated_data['user'] = user
        return super().update(instance, validated_data)

    # Read data
    def retrieve(self, instance):
        user_serializer = self.fields['user']
        user_data = user_serializer.to_representation(instance.user)
        ret = super().retrieve(instance)
        ret.data['user'] = user_data
        return ret


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
