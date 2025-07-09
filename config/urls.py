from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from config import settings
from core import views
from core.views import InfoUser
from core.urls import urlpatterns as core_urls

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += core_urls