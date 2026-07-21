from rest_framework import serializers

from common.models import FAQ, SiteSettings, StatisticCard, WhyUsCard, ProcessCard, Monitor, MonitorPriceRow, Partner


# FAQ CRUD
class AdminFAQAPIViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class AdminFAQCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'
# SiteSettings
class AdminSiteSettingsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields ="__all__"

class AdminSiteSettingsCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = '__all__'
# StatisticCard
class AdminStatisticCardListSerializers(serializers.ModelSerializer):
    class Meta:
        model = StatisticCard
        fields = '__all__'

class AdminSiteStatisticCardCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = StatisticCard
        fields = '__all__'

# WhyUsCard
class AdminWhyUsCardListSerializers(serializers.ModelSerializer):
    class Meta:
        model = WhyUsCard
        fields = '__all__'


class AdminWhyUsCardCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = WhyUsCard
        fields = '__all__'

# ProcessCard
class AdminProcessCardListSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProcessCard
        fields = '__all__'


class AdminProcessCardCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProcessCard
        fields = '__all__'

# Monitor
class AdminMonitorListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Monitor
        fields = '__all__'

class AdminMonitorCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Monitor
        fields = '__all__'

# MonitorPriceRow

class AdminMonitorPriceRowListSerializers(serializers.ModelSerializer):
    class Meta:
        model = MonitorPriceRow
        fields = '__all__'


class AdminMonitorPriceRowCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = MonitorPriceRow
        fields = '__all__'

# Partner

class AdminPartnerListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'



class AdminPartnerCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'

# MONITORS CRUD