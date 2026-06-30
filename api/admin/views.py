from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny

from api.admin.serializers import *
from common.models import FAQ


class AdminFAQListAPIView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQListSerializers
    permission_classes = [AllowAny,]
    # permission_classes = [permissions.IsAdminUse

class AdminFAQCreateAPIView(generics.CreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQCreateSerializers
    permission_classes = [AllowAny,]
    # permission_classes = [permissions.IsAdminUser]