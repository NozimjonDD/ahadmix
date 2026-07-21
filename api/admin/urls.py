from django.urls import path

from api.admin.views import *

urlpatterns = [

# SiteSettings
    path('sitesettings/list', AdminSiteSettingsListAPIView.as_view()),
    path('/create', AdminSiteSettingsCreateAPIView.as_view()),
    path('site-settings/', AdminSiteSettingsUpdateDeleteAPIView.as_view(), name='site-settings'),

# StatisticCard
    path('statisticsard/list', AdminStatisticCardListAPIView.as_view()),
    path('/create', AdminStatisticCardCreateAPIView.as_view()),
    path('statistic-card/<int:pk>/', AdminStatisticCardUpdateDeleteAPIView.as_view(), name='statistic-card-update-delete'),

# WhyUsCard
    path('whyuscard/list', AdminWhyUsCardListAPIView.as_view()),
    path('/create', AdminWhyUsCardCreateAPIView.as_view()),
    path('why-us-card/<int:pk>/', AdminWhyUsCardUpdateDeleteAPIView.as_view(), name='why-us-card-update-delete'),

# ProcessCard
    path('processcard/list', AdminProcessCardListAPIView.as_view()),
    path('/create', AdminProcessCardCreateAPIView.as_view()),
    path('process-card/<int:pk>/', AdminProcessCardUpdateDeleteAPIView.as_view(), name='process-card-update-delete'),

# Monitor
    path('monitor/list', AdminMonitorListAPIView.as_view()),
    path('/create', AdminMonitorCreateAPIView.as_view()),
    path('monitor/<int:pk>/', AdminMonitorUpdateDeleteAPIView.as_view(), name='monitor-update-delete'),

# MonitorPriceRow
    path('monitorPriceRow/list', AdminMonitorPriceRowListAPIView.as_view()),
    path('/create', AdminMonitorPriceRowCreateAPIView.as_view()),
    path('monitor/price/row/<int:pk>/', AdminMonitorPriceRowUpdateDeleteAPIView.as_view(), name='monitor-price-row-update-delete'),

# Partner
    path('partner/list', AdminPartnerListAPIView.as_view()),
    path('/create', AdminPartnerCreateAPIView.as_view()),
    path('partner/<int:pk>/', AdminPartnerUpdateDeleteAPIView.as_view(), name='partner-update-delete'),



# FAQ
    path('faq/list/', AdminFAQListAPIView.as_view()),
    path('faq/create/', AdminFAQCreateAPIView.as_view()),
    path('faq/<int:pk>/', AdminFAQUpdateDeleteAPIView.as_view(), name='faq-update-delete')

]
