from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

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

class AdminFAQUpdateDeleteAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(FAQ, pk=pk)

    def put(self, request, *args, **kwargs):

        pk = kwargs.get('pk')
        faq = get_object_or_404(FAQ, pk=pk)

        faq.question_ru = request.data.get('question_ru', faq.question_ru)
        faq.question_uz = request.data.get('question_uz', faq.question_uz)
        faq.question_en = request.data.get('question_en', faq.question_en)

        faq.answer_ru = request.data.get('answer_ru', faq.answer_ru)
        faq.answer_uz = request.data.get('answer_uz', faq.answer_uz)
        faq.answer_en = request.data.get('answer_en', faq.answer_en)

        faq.order = request.data.get('order', faq.order)
        faq.is_active = request.data.get('is_active', faq.is_active)

        faq.save()

        return Response({
            "id": faq.id,
            "question_ru": faq.question_ru,
            "question_uz": faq.question_uz,
            "question_en": faq.question_en,
            "answer_ru": faq.answer_ru,
            "answer_uz": faq.answer_uz,
            "answer_en": faq.answer_en,
            "order": faq.order,
            "is_active": faq.is_active,
        }, status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        faq = self.get_object(pk)
        faq.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdminSiteSettingsListAPIView(generics.ListAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = AdminSiteSettingsListSerializers
    permission_classes = [AllowAny, ]


class AdminSiteSettingsCreateAPIView(generics.CreateAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = AdminSiteSettingsCreateSerializers
    permission_classes = [AllowAny,]

class AdminSiteSettingsUpdateDeleteAPIView(APIView):

    def get_object(self):
        return SiteSettings.load()

    def put(self, request, *args, **kwargs):
        settings = self.get_object()

        settings.phone = request.data.get('phone', settings.phone)
        settings.email = request.data.get('email', settings.email)

        settings.address_ru = request.data.get('address_ru', settings.address_ru)
        settings.address_uz = request.data.get('address_uz', settings.address_uz)
        settings.address_en = request.data.get('address_en', settings.address_en)

        settings.telegram_link = request.data.get('telegram_link', settings.telegram_link)

        settings.screens_count = request.data.get('screens_count', settings.screens_count)
        settings.years_on_market = request.data.get('years_on_market', settings.years_on_market)
        settings.brand_partners_count = request.data.get('brand_partners_count', settings.brand_partners_count)

        if 'kp_pdf' in request.FILES:
            settings.kp_pdf = request.FILES['kp_pdf']

        settings.save()

        return Response(self.serialize(settings), status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        settings = self.get_object()
        settings.kp_pdf.delete(save=False)
        settings.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def serialize(self, settings):
        return {
            "phone": settings.phone,
            "email": settings.email,
            "address_ru": settings.address_ru,
            "address_uz": settings.address_uz,
            "address_en": settings.address_en,
            "telegram_link": settings.telegram_link,
            "screens_count": settings.screens_count,
            "years_on_market": settings.years_on_market,
            "brand_partners_count": settings.brand_partners_count,
            "kp_pdf": settings.kp_pdf.url if settings.kp_pdf else None,
        }

class AdminStatisticCardListAPIView(generics.ListAPIView):
    queryset = StatisticCard.objects.all()
    serializer_class = AdminStatisticCardListSerializers
    permission_classes = [AllowAny,]


class AdminStatisticCardCreateAPIView(generics.CreateAPIView):
    queryset = WhyUsCard.objects.all()
    serializer_class = AdminSiteStatisticCardCreateSerializers
    permission_classes = [AllowAny,]


class AdminStatisticCardUpdateDeleteAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(StatisticCard, pk=pk)

    def put(self, request, pk, *args, **kwargs):
        card = self.get_object(pk)

        card.count = request.data.get('count', card.count)
        card.title_ru = request.data.get('title_ru', card.title_ru)
        card.title_uz = request.data.get('title_uz', card.title_uz)
        card.title_en = request.data.get('title_en', card.title_en)
        card.plus = request.data.get('plus', card.plus)
        card.order = request.data.get('order', card.order)

        card.save()

        return Response(self.serialize(card), status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        card = self.get_object(pk)
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def serialize(self, card):
        return {
            "id": card.id,
            "count": card.count,
            "title_ru": card.title_ru,
            "title_uz": card.title_uz,
            "title_en": card.title_en,
            "plus": card.plus,
            "order": card.order,
        }


class AdminWhyUsCardListAPIView(generics.ListAPIView):
    queryset = WhyUsCard.objects.all()
    serializer_class = AdminWhyUsCardListSerializers
    permission_classes = [AllowAny,]


class AdminWhyUsCardCreateAPIView(generics.CreateAPIView):
    queryset = WhyUsCard.objects.all()
    serializer_class = AdminWhyUsCardCreateSerializers
    permission_classes = [AllowAny,]



class AdminWhyUsCardUpdateDeleteAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(WhyUsCard, pk=pk)

    def put(self, request, pk, *args, **kwargs):
        card = self.get_object(pk)

        card.icon_svg = request.data.get('icon_svg', card.icon_svg)

        card.title_ru = request.data.get('title_ru', card.title_ru)
        card.title_uz = request.data.get('title_uz', card.title_uz)
        card.title_en = request.data.get('title_en', card.title_en)

        card.description_ru = request.data.get('description_ru', card.description_ru)
        card.description_uz = request.data.get('description_uz', card.description_uz)
        card.description_en = request.data.get('description_en', card.description_en)

        card.order = request.data.get('order', card.order)

        card.save()

        return Response(self.serialize(card), status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        card = self.get_object(pk)
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def serialize(self, card):
        return {
            "id": card.id,
            "icon_svg": card.icon_svg,
            "title_ru": card.title_ru,
            "title_uz": card.title_uz,
            "title_en": card.title_en,
            "description_ru": card.description_ru,
            "description_uz": card.description_uz,
            "description_en": card.description_en,
            "order": card.order,
        }

class AdminProcessCardListAPIView(generics.ListAPIView):
    queryset = ProcessCard.objects.all()
    serializer_class =AdminProcessCardListSerializers
    permission_classes = [AllowAny,]


class AdminProcessCardCreateAPIView(generics.CreateAPIView):
    queryset = ProcessCard.objects.all()
    serializer_class = AdminMonitorCreateSerializers
    permission_classes = [AllowAny,]



class AdminProcessCardUpdateDeleteAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(ProcessCard, pk=pk)

    def put(self, request, pk, *args, **kwargs):
        card = self.get_object(pk)

        card.number = request.data.get('number', card.number)

        card.title_ru = request.data.get('title_ru', card.title_ru)
        card.title_uz = request.data.get('title_uz', card.title_uz)
        card.title_en = request.data.get('title_en', card.title_en)

        card.description_ru = request.data.get('description_ru', card.description_ru)
        card.description_uz = request.data.get('description_uz', card.description_uz)
        card.description_en = request.data.get('description_en', card.description_en)

        card.save()

        return Response(self.serialize(card), status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        card = self.get_object(pk)
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def serialize(self, card):
        return {
            "id": card.id,
            "number": card.number,
            "title_ru": card.title_ru,
            "title_uz": card.title_uz,
            "title_en": card.title_en,
            "description_ru": card.description_ru,
            "description_uz": card.description_uz,
            "description_en": card.description_en,
        }

class AdminMonitorListAPIView(generics.ListAPIView):
    queryset = Monitor.objects.all()
    serializer_class =AdminMonitorListSerializers
    permission_classes = [AllowAny,]


class AdminMonitorCreateAPIView(generics.CreateAPIView):
    queryset = Monitor.objects.all()
    serializer_class = AdminMonitorCreateSerializers
    permission_classes = [AllowAny,]



class AdminMonitorUpdateDeleteAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Monitor, pk=pk)

    def put(self, request, pk, *args, **kwargs):
        monitor = self.get_object(pk)

        monitor.title = request.data.get('title', monitor.title)
        monitor.title_uz = request.data.get('title_uz', monitor.title_uz)
        monitor.title_en = request.data.get('title_en', monitor.title_en)

        monitor.location = request.data.get('location', monitor.location)
        monitor.location_uz = request.data.get('location_uz', monitor.location_uz)
        monitor.location_en = request.data.get('location_en', monitor.location_en)

        monitor.district = request.data.get('district', monitor.district)

        monitor.size = request.data.get('size', monitor.size)
        monitor.format = request.data.get('format', monitor.format)
        monitor.type_display = request.data.get('type_display', monitor.type_display)
        monitor.resolution = request.data.get('resolution', monitor.resolution)
        monitor.broadcast_hours = request.data.get('broadcast_hours', monitor.broadcast_hours)

        monitor.category = request.data.get('category', monitor.category)
        monitor.status = request.data.get('status', monitor.status)

        monitor.latitude = request.data.get('latitude', monitor.latitude)
        monitor.longitude = request.data.get('longitude', monitor.longitude)

        monitor.is_featured = request.data.get('is_featured', monitor.is_featured)
        monitor.is_in_ticker = request.data.get('is_in_ticker', monitor.is_in_ticker)
        monitor.is_active = request.data.get('is_active', monitor.is_active)

        monitor.order = request.data.get('order', monitor.order)

        if 'image' in request.FILES:
            monitor.image = request.FILES['image']

        if 'video' in request.FILES:
            monitor.video = request.FILES['video']

        monitor.save()

        return Response(self.serialize(monitor), status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        monitor = self.get_object(pk)
        monitor.image.delete(save=False) if monitor.image else None
        monitor.video.delete(save=False) if monitor.video else None
        monitor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def serialize(self, monitor):
        return {
            "id": monitor.id,
            "title": monitor.title,
            "title_uz": monitor.title_uz,
            "title_en": monitor.title_en,
            "location": monitor.location,
            "location_uz": monitor.location_uz,
            "location_en": monitor.location_en,
            "district": monitor.district,
            "size": monitor.size,
            "format": monitor.format,
            "type_display": monitor.type_display,
            "resolution": monitor.resolution,
            "broadcast_hours": monitor.broadcast_hours,
            "category": monitor.category,
            "status": monitor.status,
            "image": monitor.image.url if monitor.image else None,
            "video": monitor.video.url if monitor.video else None,
            "latitude": monitor.latitude,
            "longitude": monitor.longitude,
            "is_featured": monitor.is_featured,
            "is_in_ticker": monitor.is_in_ticker,
            "is_active": monitor.is_active,
            "order": monitor.order,
        }


class AdminMonitorPriceRowListAPIView(generics.ListAPIView):
    queryset = MonitorPriceRow.objects.all()
    serializer_class =AdminMonitorPriceRowListSerializers
    permission_classes = [AllowAny,]


class AdminMonitorPriceRowCreateAPIView(generics.CreateAPIView):
    queryset = MonitorPriceRow.objects.all()
    serializer_class = AdminMonitorPriceRowCreateSerializers
    permission_classes = [AllowAny,]



class AdminMonitorPriceRowUpdateDeleteAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(MonitorPriceRow, pk=pk)

    def put(self, request, pk, *args, **kwargs):
        row = self.get_object(pk)

        monitor_id = request.data.get('monitor')
        if monitor_id:
            row.monitor = get_object_or_404(Monitor, pk=monitor_id)

        row.duration = request.data.get('duration', row.duration)
        row.plays_per_month = request.data.get('plays_per_month', row.plays_per_month)
        row.price = request.data.get('price', row.price)
        row.order = request.data.get('order', row.order)

        row.save()

        return Response(self.serialize(row), status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        row = self.get_object(pk)
        row.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def serialize(self, row):
        return {
            "id": row.id,
            "monitor": row.monitor_id,
            "duration": row.duration,
            "plays_per_month": row.plays_per_month,
            "price": row.price,
            "order": row.order,
        }


class AdminPartnerListAPIView(generics.ListAPIView):
    queryset = Partner.objects.all()
    serializer_class =AdminPartnerListSerializers
    permission_classes = [AllowAny,]


class AdminPartnerCreateAPIView(generics.CreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = AdminPartnerCreateSerializers
    permission_classes = [AllowAny,]


class AdminPartnerUpdateDeleteAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Partner, pk=pk)

    def put(self, request, pk, *args, **kwargs):
        partner = self.get_object(pk)

        partner.name = request.data.get('name', partner.name)
        partner.order = request.data.get('order', partner.order)
        partner.is_active = request.data.get('is_active', partner.is_active)

        if 'logo' in request.FILES:
            partner.logo = request.FILES['logo']

        partner.save()

        return Response(self.serialize(partner), status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        partner = self.get_object(pk)
        partner.logo.delete(save=False) if partner.logo else None
        partner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def serialize(self, partner):
        return {
            "id": partner.id,
            "name": partner.name,
            "logo": partner.logo.url if partner.logo else None,
            "order": partner.order,
            "is_active": partner.is_active,
        }