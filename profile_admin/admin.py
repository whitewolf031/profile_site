from django.contrib import admin
from core.models import UserInfo

@admin.register(UserInfo)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'phone_number', 'location', 'birth_date']
    search_fields = ['user__username', 'location']
    list_filter = ['location']
