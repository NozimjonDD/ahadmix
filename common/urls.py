from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from common.views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]

