from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User
from unfold.admin import ModelAdmin, TabularInline
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

from .models import (
    SiteSettings, StatisticCard, WhyUsCard, ProcessCard,
    Monitor, MonitorPriceRow, Partner, FAQ
)


@admin.register(SiteSettings)
class SiteSettingsAdmin(ModelAdmin):
    fieldsets = (
        ("Aloqa", {"fields": ("phone", "email", "telegram_link")}),
        ("Manzil", {"fields": ("address_ru", "address_uz", "address_en")}),
        ("Hero stats", {"fields": ("screens_count", "years_on_market", "brand_partners_count")}),
        ("Hujjatlar", {"fields": ("kp_pdf",)}),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(StatisticCard)
class StatisticCardAdmin(ModelAdmin):
    list_display = ("order", "count", "title_ru", "plus")
    list_editable = ("count", "title_ru", "plus")
    ordering = ("order",)


@admin.register(WhyUsCard)
class WhyUsCardAdmin(ModelAdmin):
    list_display = ("order", "title_ru")
    list_editable = ("title_ru",)
    ordering = ("order",)


@admin.register(ProcessCard)
class ProcessCardAdmin(ModelAdmin):
    list_display = ("number", "title_ru")
    ordering = ("number",)


class MonitorPriceRowInline(TabularInline):
    model = MonitorPriceRow
    extra = 1


@admin.register(Monitor)
class MonitorAdmin(ModelAdmin):
    list_display = ("order", "title", "size", "category", "status",
                    "is_featured", "is_in_ticker", "is_active")
    list_editable = ("is_featured", "is_in_ticker", "is_active", "status")
    list_filter = ("category", "status", "is_featured", "is_in_ticker", "is_active")
    search_fields = ("title", "title_uz", "title_en", "location")
    inlines = [MonitorPriceRowInline]
    fieldsets = (
        ("Asosiy", {"fields": ("title", "title_uz", "title_en", "category", "status")}),
        ("Manzil", {"fields": ("location", "location_uz", "location_en", "district",
                               "latitude", "longitude")}),
        ("Texnik", {"fields": ("size", "format", "type_display", "resolution",
                               "broadcast_hours")}),
        ("Media", {"fields": ("image", "video")}),
        ("Ko'rinish", {"fields": ("is_featured", "is_in_ticker", "is_active", "order")}),
    )


@admin.register(Partner)
class PartnerAdmin(ModelAdmin):
    list_display = ("order", "name", "is_active")
    list_editable = ("is_active",)
    list_filter = ("is_active",)
    search_fields = ("name",)


@admin.register(FAQ)
class FAQAdmin(ModelAdmin):
    list_display = ("order", "question_ru", "is_active")
    list_editable = ("is_active",)
    list_filter = ("is_active",)
    search_fields = ("question_ru",)


@admin.register(MonitorPriceRow)
class MonitorPriceRowAdmin(ModelAdmin):
    list_display = ('monitor', 'duration', 'plays_per_month', 'price', 'order')
    list_filter = ('monitor',)
    search_fields = ('monitor__title', 'duration')
    ordering = ['order']

# Django's built-in auth admins subclass the stock ModelAdmin, so they render
# unstyled inside Unfold. Re-register them against Unfold's base + forms.
admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass
