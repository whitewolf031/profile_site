from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from core.models import UserInfo
from core.serializers import TakeUserInfo


class InfoUser(generics.ListAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = TakeUserInfo
    permission_classes = [AllowAny]