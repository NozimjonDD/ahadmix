from django.urls import path

from api.admin.views import *

urlpatterns = [
    # FAQ
    path('faq/list/', AdminFAQListAPIView.as_view()),
    path('create/', AdminFAQCreateAPIView.as_view()),

    # MONITOR
    # path('manitor/list/', Adm????tAPIView.as_view()),


]
