from django.urls import path

from api.admin.views import (
    AdminSiteSettingsListAPIView, AdminSiteSettingsCreateAPIView,
    AdminStatisticCardListAPIView, AdminStatisticCardCreateAPIView,
    AdminWhyUsCardListAPIView, AdminWhyUsCardCreateAPIView,
    AdminProcessCardListAPIView, AdminProcessCardCreateAPIView,
    AdminMonitorListAPIView, AdminMonitorCreateAPIView,
    AdminMonitorPriceRowListAPIView, AdminMonitorPriceRowCreateAPIView,
    AdminPartnerListAPIView, AdminPartnerCreateAPIView,
    AdminFAQListAPIView, AdminFAQCreateAPIView,
)

app_name = 'api-admin'

urlpatterns = [
    # SiteSettings
    path('sitesettings/list/', AdminSiteSettingsListAPIView.as_view(), name='sitesettings-list'),
    path('sitesettings/create/', AdminSiteSettingsCreateAPIView.as_view(), name='sitesettings-create'),

    # StatisticCard
    path('statisticcard/list/', AdminStatisticCardListAPIView.as_view(), name='statisticcard-list'),
    path('statisticcard/create/', AdminStatisticCardCreateAPIView.as_view(), name='statisticcard-create'),

    # WhyUsCard
    path('whyuscard/list/', AdminWhyUsCardListAPIView.as_view(), name='whyuscard-list'),
    path('whyuscard/create/', AdminWhyUsCardCreateAPIView.as_view(), name='whyuscard-create'),

    # ProcessCard
    path('processcard/list/', AdminProcessCardListAPIView.as_view(), name='processcard-list'),
    path('processcard/create/', AdminProcessCardCreateAPIView.as_view(), name='processcard-create'),

    # Monitor
    path('monitor/list/', AdminMonitorListAPIView.as_view(), name='monitor-list'),
    path('monitor/create/', AdminMonitorCreateAPIView.as_view(), name='monitor-create'),

    # MonitorPriceRow
    path('monitorpricerow/list/', AdminMonitorPriceRowListAPIView.as_view(), name='monitorpricerow-list'),
    path('monitorpricerow/create/', AdminMonitorPriceRowCreateAPIView.as_view(), name='monitorpricerow-create'),

    # Partner
    path('partner/list/', AdminPartnerListAPIView.as_view(), name='partner-list'),
    path('partner/create/', AdminPartnerCreateAPIView.as_view(), name='partner-create'),

    # FAQ
    path('faq/list/', AdminFAQListAPIView.as_view(), name='faq-list'),
    path('faq/create/', AdminFAQCreateAPIView.as_view(), name='faq-create'),
]
