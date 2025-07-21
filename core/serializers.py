from rest_framework import serializers
from core.models import UserInfo

class TakeUserInfo(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['full_name', 'email_address', 'phone_number', 'subject', 'message']
