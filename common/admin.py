from django.contrib import admin

from .models import District, Region


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
