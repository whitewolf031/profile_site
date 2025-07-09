from django.contrib import admin
from django.urls import path

from core.views import InfoUser

urlpatterns = [
    path('menu/', InfoUser.as_view(), name='infouser'),
]