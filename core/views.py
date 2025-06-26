from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from core.models import UserInfo

class InfoUser(ModelViewSet):