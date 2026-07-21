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

# Permission policy: AllowAny on everything, set once via
# REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] in settings.py. No view overrides
# it, so read AND write are open to anonymous users. See the note in settings.py
# before deploying.
#
# The serializers still handle validation, so invalid input returns 400 rather
# than crashing or silently storing an out-of-choices value.


# FAQ
class AdminFAQListAPIView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = AdminFAQAPIViewSerializers


class AdminFAQCreateAPIView(generics.CreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = AdminFAQCreateSerializers


class AdminFAQUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = AdminFAQCreateSerializers


# SiteSettings
class AdminSiteSettingsListAPIView(generics.ListAPIView):
    # SiteSettings has no Meta.ordering; order explicitly so pagination is stable.
    queryset = SiteSettings.objects.order_by('pk')
    serializer_class = AdminSiteSettingsListSerializers


class AdminSiteSettingsCreateAPIView(generics.CreateAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = AdminSiteSettingsCreateSerializers


class AdminSiteSettingsUpdateDeleteAPIView(generics.RetrieveUpdateAPIView):
    """Singleton — always resolves to the one row, so it takes no pk.

    Intentionally RetrieveUpdate (not Destroy): deleting site settings wipes the
    site's phone, email, addresses and KP file. common.admin.SiteSettingsAdmin
    sets has_delete_permission = False for the same reason, so DELETE here
    returns 405 rather than contradicting the admin.
    """
    serializer_class = AdminSiteSettingsCreateSerializers

    def get_object(self):
        return SiteSettings.load()


# StatisticCard
class AdminStatisticCardListAPIView(generics.ListAPIView):
    queryset = StatisticCard.objects.all()
    serializer_class = AdminStatisticCardListSerializers


class AdminStatisticCardCreateAPIView(generics.CreateAPIView):
    queryset = StatisticCard.objects.all()
    serializer_class = AdminSiteStatisticCardCreateSerializers


class AdminStatisticCardUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StatisticCard.objects.all()
    serializer_class = AdminSiteStatisticCardCreateSerializers


# WhyUsCard
class AdminWhyUsCardListAPIView(generics.ListAPIView):
    queryset = WhyUsCard.objects.all()
    serializer_class = AdminWhyUsCardListSerializers


class AdminWhyUsCardCreateAPIView(generics.CreateAPIView):
    queryset = WhyUsCard.objects.all()
    serializer_class = AdminWhyUsCardCreateSerializers


class AdminWhyUsCardUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WhyUsCard.objects.all()
    serializer_class = AdminWhyUsCardCreateSerializers


# ProcessCard
class AdminProcessCardListAPIView(generics.ListAPIView):
    queryset = ProcessCard.objects.all()
    serializer_class = AdminProcessCardListSerializers


class AdminProcessCardCreateAPIView(generics.CreateAPIView):
    queryset = ProcessCard.objects.all()
    serializer_class = AdminProcessCardCreateSerializers


class AdminProcessCardUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProcessCard.objects.all()
    serializer_class = AdminProcessCardCreateSerializers


# Monitor
class AdminMonitorListAPIView(generics.ListAPIView):
    queryset = Monitor.objects.all()
    serializer_class = AdminMonitorListSerializers


class AdminMonitorCreateAPIView(generics.CreateAPIView):
    queryset = Monitor.objects.all()
    serializer_class = AdminMonitorCreateSerializers


class AdminMonitorUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Monitor.objects.all()
    serializer_class = AdminMonitorCreateSerializers


# MonitorPriceRow
class AdminMonitorPriceRowListAPIView(generics.ListAPIView):
    queryset = MonitorPriceRow.objects.select_related('monitor')
    serializer_class = AdminMonitorPriceRowListSerializers


class AdminMonitorPriceRowCreateAPIView(generics.CreateAPIView):
    queryset = MonitorPriceRow.objects.all()
    serializer_class = AdminMonitorPriceRowCreateSerializers


class AdminMonitorPriceRowUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MonitorPriceRow.objects.select_related('monitor')
    serializer_class = AdminMonitorPriceRowCreateSerializers


# Partner
class AdminPartnerListAPIView(generics.ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = AdminPartnerListSerializers


class AdminPartnerCreateAPIView(generics.CreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = AdminPartnerCreateSerializers


class AdminPartnerUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Partner.objects.all()
    serializer_class = AdminPartnerCreateSerializers
