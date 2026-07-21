from django.urls import path

from api.admin.views import (
    AdminSiteSettingsListAPIView, AdminSiteSettingsCreateAPIView,
    AdminSiteSettingsUpdateDeleteAPIView,
    AdminStatisticCardListAPIView, AdminStatisticCardCreateAPIView,
    AdminStatisticCardUpdateDeleteAPIView,
    AdminWhyUsCardListAPIView, AdminWhyUsCardCreateAPIView,
    AdminWhyUsCardUpdateDeleteAPIView,
    AdminProcessCardListAPIView, AdminProcessCardCreateAPIView,
    AdminProcessCardUpdateDeleteAPIView,
    AdminMonitorListAPIView, AdminMonitorCreateAPIView,
    AdminMonitorUpdateDeleteAPIView,
    AdminMonitorPriceRowListAPIView, AdminMonitorPriceRowCreateAPIView,
    AdminMonitorPriceRowUpdateDeleteAPIView,
    AdminPartnerListAPIView, AdminPartnerCreateAPIView,
    AdminPartnerUpdateDeleteAPIView,
    AdminFAQListAPIView, AdminFAQCreateAPIView,
    AdminFAQUpdateDeleteAPIView,
)

app_name = 'api-admin'

urlpatterns = [
    # SiteSettings (singleton — the detail route takes no pk)
    path('sitesettings/list/', AdminSiteSettingsListAPIView.as_view(), name='sitesettings-list'),
    path('sitesettings/create/', AdminSiteSettingsCreateAPIView.as_view(), name='sitesettings-create'),
    path('site-settings/', AdminSiteSettingsUpdateDeleteAPIView.as_view(), name='site-settings'),

    # StatisticCard
    path('statisticcard/list/', AdminStatisticCardListAPIView.as_view(), name='statisticcard-list'),
    path('statisticcard/create/', AdminStatisticCardCreateAPIView.as_view(), name='statisticcard-create'),
    path('statistic-card/<int:pk>/', AdminStatisticCardUpdateDeleteAPIView.as_view(), name='statistic-card-update-delete'),

    # WhyUsCard
    path('whyuscard/list/', AdminWhyUsCardListAPIView.as_view(), name='whyuscard-list'),
    path('whyuscard/create/', AdminWhyUsCardCreateAPIView.as_view(), name='whyuscard-create'),
    path('why-us-card/<int:pk>/', AdminWhyUsCardUpdateDeleteAPIView.as_view(), name='why-us-card-update-delete'),

    # ProcessCard
    path('processcard/list/', AdminProcessCardListAPIView.as_view(), name='processcard-list'),
    path('processcard/create/', AdminProcessCardCreateAPIView.as_view(), name='processcard-create'),
    path('process-card/<int:pk>/', AdminProcessCardUpdateDeleteAPIView.as_view(), name='process-card-update-delete'),

    # Monitor
    path('monitor/list/', AdminMonitorListAPIView.as_view(), name='monitor-list'),
    path('monitor/create/', AdminMonitorCreateAPIView.as_view(), name='monitor-create'),
    path('monitor/<int:pk>/', AdminMonitorUpdateDeleteAPIView.as_view(), name='monitor-update-delete'),

    # MonitorPriceRow
    path('monitorpricerow/list/', AdminMonitorPriceRowListAPIView.as_view(), name='monitorpricerow-list'),
    path('monitorpricerow/create/', AdminMonitorPriceRowCreateAPIView.as_view(), name='monitorpricerow-create'),
    path('monitor/price/row/<int:pk>/', AdminMonitorPriceRowUpdateDeleteAPIView.as_view(), name='monitor-price-row-update-delete'),

    # Partner
    path('partner/list/', AdminPartnerListAPIView.as_view(), name='partner-list'),
    path('partner/create/', AdminPartnerCreateAPIView.as_view(), name='partner-create'),
    path('partner/<int:pk>/', AdminPartnerUpdateDeleteAPIView.as_view(), name='partner-update-delete'),

    # FAQ
    path('faq/list/', AdminFAQListAPIView.as_view(), name='faq-list'),
    path('faq/create/', AdminFAQCreateAPIView.as_view(), name='faq-create'),
    path('faq/<int:pk>/', AdminFAQUpdateDeleteAPIView.as_view(), name='faq-update-delete'),
]
