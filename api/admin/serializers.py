from rest_framework import serializers

from common.models import FAQ

# FAQ CRUD
class FAQListSerializers(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class FAQCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'




# MONITORS CRUD