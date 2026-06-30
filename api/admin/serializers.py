from rest_framework import serializers

from common.models import FAQ


class FAQSerializers(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class FAQCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'