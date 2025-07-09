from rest_framework import serializers
from core.models import UserInfo


class TakeUserInfo(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = "__all__"