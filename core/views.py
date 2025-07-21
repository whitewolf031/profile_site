from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from core.models import UserInfo
from core.serializers import TakeUserInfo
import os
import telebot
from dotenv import load_dotenv

load_dotenv()

class InfoUser(generics.CreateAPIView):  # ✅ createAPIView, not ListAPIView
    queryset = UserInfo.objects.all()
    serializer_class = TakeUserInfo
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        instance = serializer.save()
        data = instance.created_at
        date = str(data)[0:10]
        time = str(data)[11:19]

        bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
        chat_id = os.getenv("TELEGRAM_CHAT_ID")

        if not bot_token or not chat_id:
            print("❌ .env faylida TOKEN yoki CHAT_ID yo'q")
            return

        bot = telebot.TeleBot(bot_token)
        message = (
            f"📥 *Yangi Kontakt So'rovi* ({date} {time})\n\n"
            f"👤 *Ism:* {instance.full_name}\n"
            f"📧 *Email:* {instance.email_address}\n"
            f"📞 *Telefon:* {instance.phone_number}\n"
            f"📝 *Mavzu:* {instance.subject}\n"
            f"💬 *Xabar:*\n{instance.message}"
        )
        bot.send_message(chat_id, message, parse_mode='Markdown')
