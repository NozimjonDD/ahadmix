from django.contrib import admin

from .models import District, Region, TestModel, Card, Outdoor, WhyUsCard, StatisticCard
from .models import ProcessCard

from django.contrib import admin
from .models import Monitor, PricePackage



class DistrictInline(admin.TabularInline):
    model = District
    extra = 0
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name', 'slug', 'is_active', 'sort_order')


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_active', 'sort_order', 'updated_at')
    list_editable = ('is_active', 'sort_order')
    list_filter = ('is_active',)
    search_fields = ('name', 'code', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    inlines = (DistrictInline,)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'is_active', 'sort_order', 'updated_at')
    list_editable = ('is_active', 'sort_order')
    list_filter = ('region', 'is_active')
    search_fields = ('name', 'slug', 'region__name')
    prepopulated_fields = {'slug': ('name',)}
    autocomplete_fields = ('region',)


@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'count' )


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'count', )


@admin.register(Outdoor)
class OutdoorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'word','icon' )


@admin.register(StatisticCard)
class StatisticCardAdmin(admin.ModelAdmin):
    list_display = ["title_ru", "count", "order"]
    list_editable = ["count", "order"]
    ordering = ["order"]

@admin.register(WhyUsCard)
class WhyUsCardAdmin(admin.ModelAdmin):
    list_display = ('order', 'title', 'is_active', 'updated_at')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    ordering = ('order',)
    list_display_links = ('title',)


@admin.register(ProcessCard)
class ProcessCardAdmin(admin.ModelAdmin):
    list_display = ['number', 'title', 'created_at']
    list_display_links = ['title']
    search_fields = ['title', 'description']
    list_filter = ['number']


@admin.register(Monitor)
class MonitorAdmin(admin.ModelAdmin):
    list_display = ["title", "region", "screen_size"]
    search_fields = ["title", "address"]


@admin.register(PricePackage)
class PricePackageAdmin(admin.ModelAdmin):
    list_display = ["led_screen", "duration", "price"]












