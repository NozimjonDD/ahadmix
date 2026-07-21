from rest_framework import generics

from api.admin.serializers import (
    AdminFAQAPIViewSerializers,
    AdminFAQCreateSerializers,
    AdminSiteSettingsListSerializers,
    AdminSiteSettingsCreateSerializers,
    AdminStatisticCardListSerializers,
    AdminSiteStatisticCardCreateSerializers,
    AdminWhyUsCardListSerializers,
    AdminWhyUsCardCreateSerializers,
    AdminProcessCardListSerializers,
    AdminProcessCardCreateSerializers,
    AdminMonitorListSerializers,
    AdminMonitorCreateSerializers,
    AdminMonitorPriceRowListSerializers,
    AdminMonitorPriceRowCreateSerializers,
    AdminPartnerListSerializers,
    AdminPartnerCreateSerializers,
)
from common.models import (
    FAQ, SiteSettings, StatisticCard, WhyUsCard, ProcessCard,
    Monitor, MonitorPriceRow, Partner,
)

# Permissions come from REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] (IsAdminUser).
# Do not set permission_classes = [AllowAny] here — these endpoints expose write
# access to every piece of site content.


# FAQ
class AdminFAQListAPIView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = AdminFAQAPIViewSerializers


class AdminFAQCreateAPIView(generics.CreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = AdminFAQCreateSerializers


# SiteSettings
class AdminSiteSettingsListAPIView(generics.ListAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = AdminSiteSettingsListSerializers


class AdminSiteSettingsCreateAPIView(generics.CreateAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = AdminSiteSettingsCreateSerializers


# StatisticCard
class AdminStatisticCardListAPIView(generics.ListAPIView):
    queryset = StatisticCard.objects.all()
    serializer_class = AdminStatisticCardListSerializers


class AdminStatisticCardCreateAPIView(generics.CreateAPIView):
    queryset = StatisticCard.objects.all()
    serializer_class = AdminSiteStatisticCardCreateSerializers


# WhyUsCard
class AdminWhyUsCardListAPIView(generics.ListAPIView):
    queryset = WhyUsCard.objects.all()
    serializer_class = AdminWhyUsCardListSerializers


class AdminWhyUsCardCreateAPIView(generics.CreateAPIView):
    queryset = WhyUsCard.objects.all()
    serializer_class = AdminWhyUsCardCreateSerializers


# ProcessCard
class AdminProcessCardListAPIView(generics.ListAPIView):
    queryset = ProcessCard.objects.all()
    serializer_class = AdminProcessCardListSerializers


class AdminProcessCardCreateAPIView(generics.CreateAPIView):
    queryset = ProcessCard.objects.all()
    serializer_class = AdminProcessCardCreateSerializers


# Monitor
class AdminMonitorListAPIView(generics.ListAPIView):
    queryset = Monitor.objects.all()
    serializer_class = AdminMonitorListSerializers


class AdminMonitorCreateAPIView(generics.CreateAPIView):
    queryset = Monitor.objects.all()
    serializer_class = AdminMonitorCreateSerializers


# MonitorPriceRow
class AdminMonitorPriceRowListAPIView(generics.ListAPIView):
    queryset = MonitorPriceRow.objects.select_related('monitor')
    serializer_class = AdminMonitorPriceRowListSerializers


class AdminMonitorPriceRowCreateAPIView(generics.CreateAPIView):
    queryset = MonitorPriceRow.objects.all()
    serializer_class = AdminMonitorPriceRowCreateSerializers


# Partner
class AdminPartnerListAPIView(generics.ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = AdminPartnerListSerializers


class AdminPartnerCreateAPIView(generics.CreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = AdminPartnerCreateSerializers
