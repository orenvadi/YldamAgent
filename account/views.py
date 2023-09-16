from django.shortcuts import render
from models import *
from rest_framework import generics, permissions, serializers, status
from serializers import *


class AdministratorAPIView(generics.ListCreateAPIView):
    serializer_class = AdminSerializer


# class APIView(generics.ListCreateAPIView):
#     serializer_class = AdminSerializer
#
#
# class AdministratorAPIView(generics.ListCreateAPIView):
#     serializer_class = AdminSerializer
#
#
# class AdministratorAPIView(generics.ListCreateAPIView):
#     serializer_class = AdminSerializer
#
#
# class AdministratorAPIView(generics.ListCreateAPIView):
#     serializer_class = AdminSerializer
#
#
# class AdministratorAPIView(generics.ListCreateAPIView):
#     serializer_class = AdminSerializer
#
#
# class AdministratorAPIView(generics.ListCreateAPIView):
#     serializer_class = AdminSerializer
