from django.urls import path

from api.admin.views import *

urlpatterns = [
    path('faq/list/', AdminFAQListAPIView.as_view()),
    path('create/', AdminFAQCreateAPIView.as_view()),
]
