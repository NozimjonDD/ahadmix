from django.urls import path

from api.admin.views import *

urlpatterns = [

# SiteSettings
    path('sitesettings/list', AdminSiteSettingsListAPIView.as_view()),
    path('/create', AdminSiteSettingsCreateAPIView.as_view()),
# StatisticCard
    path('statisticsard/list', AdminStatisticCardListAPIView.as_view()),
    path('/create', AdminStatisticCardCreateAPIView.as_view()),
# WhyUsCard
    path('whyuscard/list', AdminWhyUsCardListAPIView.as_view()),
    path('/create', AdminWhyUsCardCreateAPIView.as_view()),

# ProcessCard
    path('processcard/list', AdminProcessCardListAPIView.as_view()),
    path('/create', AdminProcessCardCreateAPIView.as_view()),

# Monitor
    path('monitor/list', AdminMonitorListAPIView.as_view()),
    path('/create', AdminMonitorCreateAPIView.as_view()),
# MonitorPriceRow

    path('monitorPriceRow/list', AdminMonitorPriceRowListAPIView.as_view()),
    path('/create', AdminMonitorPriceRowCreateAPIView.as_view()),
# Partner
    path('partner/list', AdminPartnerListAPIView.as_view()),
    path('/create', AdminPartnerCreateAPIView.as_view()),

# FAQ
    path('faq/list/', AdminFAQListAPIView.as_view()),
    path('create/', AdminFAQCreateAPIView.as_view()),

]
