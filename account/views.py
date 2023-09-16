from rest_framework import generics, permissions, status
from .serializers import *
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from django.contrib.auth import login, authenticate
from rest_framework.response import Response


class SignUpAPI(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": CustomUserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class AdministratorAPIView(generics.CreateAPIView):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        company = serializer.save()
        return Response({
            "admin": AdministratorSerializer(company, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(company.user)[1]
        })


class StoreOwnerAPIView(generics.ListCreateAPIView):
    queryset = StoreOwner.objects.all()
    serializer_class = StoreOwnerSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        company = serializer.save()
        return Response({
            "store-owner": StoreOwnerSerializer(company, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(company.user)[1]
        })


class StoreManagerAPIView(generics.ListCreateAPIView):
    queryset = StoreManager.objects.all()
    serializer_class = StoreManagerSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        company = serializer.save()
        return Response({
            "store-manager": StoreManagerSerializer(company, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(company.user)[1]
        })


class ProducerAPIView(generics.ListCreateAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        company = serializer.save()
        return Response({
            "company": ProducerSerializer(company, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(company.user)[1]
        })


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


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            serialized_user = CustomUserSerializer(user)
            return Response({
                "user": serialized_user.data,
                "token": AuthToken.objects.create(user)[1]
            })
        else:
            return Response({
                "error": "Invalid credentials"
            }, status=status.HTTP_401_UNAUTHORIZED)
