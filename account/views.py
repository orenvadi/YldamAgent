from rest_framework import generics
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


# class LoginAPI(KnoxLoginView):
#     permission_classes = (permissions.AllowAny,)
#
#     def post(self, request, format=None):
#         email = request.data.get('email')
#         password = request.data.get('password')
#         user = authenticate(request, username=email, password=password)
#
#         if user is not None:
#             login(request, user)
#             serialized_user = CustomUserSerializer(user)
#             return Response({
#                 "user": serialized_user.data,
#                 "token": AuthToken.objects.create(user)[1]
#             })
#         else:
#             return Response({
#                 "error": "Invalid credentials"
#             }, status=status.HTTP_401_UNAUTHORIZED)


# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#
#         user = User.objects.get(username=username)
#
#         if user.check_password(password):
#             jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#             jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
#
#             payload = jwt_payload_handler(user)
#             token = jwt_encode_handler(payload)
#
#             return Response({'token': token})
#         else:
#             return Response({'error': 'Неверное имя пользователя или пароль'}, status=status.HTTP_401_UNAUTHORIZED)
