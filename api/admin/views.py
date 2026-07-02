from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny

from api.admin.serializers import *
from common.models import FAQ, SiteSettings, StatisticCard, WhyUsCard, ProcessCard, Monitor


class AdminFAQListAPIView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = AdminFAQAPIViewSerializers
    permission_classes = [AllowAny,]
    # permission_classes = [permissions.IsAdminUse

class AdminFAQCreateAPIView(generics.CreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = AdminFAQCreateSerializers
    permission_classes = [AllowAny,]
    # permission_classes = [permissions.IsAdminUser]

class AdminSiteSettingsListAPIView(generics.ListAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = AdminSiteSettingsListSerializers
    permission_classes = [AllowAny, ]


class AdminSiteSettingsCreateAPIView(generics.CreateAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = AdminSiteSettingsCreateSerializers
    permission_classes = [AllowAny,]


class AdminStatisticCardListAPIView(generics.ListAPIView):
    queryset = StatisticCard.objects.all()
    serializer_class = AdminStatisticCardListSerializers
    permission_classes = [AllowAny,]


class AdminStatisticCardCreateAPIView(generics.CreateAPIView):
    queryset = WhyUsCard.objects.all()
    serializer_class = AdminSiteStatisticCardCreateSerializers
    permission_classes = [AllowAny,]


class AdminWhyUsCardListAPIView(generics.ListAPIView):
    queryset = WhyUsCard.objects.all()
    serializer_class = AdminWhyUsCardListSerializers
    permission_classes = [AllowAny,]


class AdminWhyUsCardCreateAPIView(generics.CreateAPIView):
    queryset = WhyUsCard.objects.all()
    serializer_class = AdminWhyUsCardCreateSerializers
    permission_classes = [AllowAny,]


class AdminProcessCardListAPIView(generics.ListAPIView):
    queryset = ProcessCard.objects.all()
    serializer_class =AdminProcessCardListSerializers
    permission_classes = [AllowAny,]


class AdminProcessCardCreateAPIView(generics.CreateAPIView):
    queryset = ProcessCard.objects.all()
    serializer_class = AdminMonitorCreateSerializers
    permission_classes = [AllowAny,]


class AdminMonitorListAPIView(generics.ListAPIView):
    queryset = Monitor.objects.all()
    serializer_class =AdminMonitorListSerializers
    permission_classes = [AllowAny,]


class AdminMonitorCreateAPIView(generics.CreateAPIView):
    queryset = Monitor.objects.all()
    serializer_class = AdminMonitorCreateSerializers
    permission_classes = [AllowAny,]


class AdminMonitorPriceRowListAPIView(generics.ListAPIView):
    queryset = MonitorPriceRow.objects.all()
    serializer_class =AdminMonitorPriceRowListSerializers
    permission_classes = [AllowAny,]


class AdminMonitorPriceRowCreateAPIView(generics.CreateAPIView):
    queryset = MonitorPriceRow.objects.all()
    serializer_class = AdminMonitorPriceRowCreateSerializers
    permission_classes = [AllowAny,]



class AdminPartnerListAPIView(generics.ListAPIView):
    queryset = Partner.objects.all()
    serializer_class =AdminPartnerListSerializers
    permission_classes = [AllowAny,]



class AdminPartnerCreateAPIView(generics.CreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = AdminPartnerCreateSerializers
    permission_classes = [AllowAny,]

