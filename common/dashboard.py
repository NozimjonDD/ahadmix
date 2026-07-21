"""Admin dashboard data for Unfold.

Wired via UNFOLD["DASHBOARD_CALLBACK"] in settings.py. Unfold calls this with
(request, context) and uses whatever context is returned to render
templates/admin/index.html.
"""

from django.urls import reverse

from .models import (
    FAQ,
    Monitor,
    MonitorPriceRow,
    Partner,
    ProcessCard,
    SiteSettings,
    StatisticCard,
    WhyUsCard,
)


def _changelist(model) -> str:
    """URL of a model's admin changelist."""
    meta = model._meta
    return reverse(f"admin:{meta.app_label}_{meta.model_name}_changelist")


def dashboard_callback(request, context):
    # One aggregate pass per model rather than repeated .count() calls in the
    # template, so the page stays at a fixed, small number of queries.
    monitors_total = Monitor.objects.count()
    monitors_active = Monitor.objects.filter(is_active=True).count()
    monitors_live = Monitor.objects.filter(status="live", is_active=True).count()
    monitors_soon = Monitor.objects.filter(status="soon", is_active=True).count()
    monitors_featured = Monitor.objects.filter(is_featured=True, is_active=True).count()
    monitors_mapped = (
        Monitor.objects.filter(is_active=True)
        .exclude(latitude__isnull=True)
        .exclude(longitude__isnull=True)
        .count()
    )

    partners_total = Partner.objects.count()
    partners_active = Partner.objects.filter(is_active=True).count()

    faq_total = FAQ.objects.count()
    faq_active = FAQ.objects.filter(is_active=True).count()

    price_rows = MonitorPriceRow.objects.count()

    # Headline metrics — the four numbers worth seeing first.
    context["kpis"] = [
        {
            "title": "Ekranlar",
            "value": monitors_total,
            "meta": f"{monitors_active} faol · {monitors_soon} tez kunda",
            "icon": "tv",
            "link": _changelist(Monitor),
        },
        {
            "title": "Efirdagi ekranlar",
            "value": monitors_live,
            "meta": f"{monitors_featured} tanlangan · {monitors_mapped} xaritada",
            "icon": "sensors",
            "link": _changelist(Monitor) + "?status__exact=live",
        },
        {
            "title": "Hamkorlar",
            "value": partners_total,
            "meta": f"{partners_active} faol",
            "icon": "handshake",
            "link": _changelist(Partner),
        },
        {
            "title": "Narx qatorlari",
            "value": price_rows,
            "meta": "Barcha ekranlar bo'yicha",
            "icon": "sell",
            "link": _changelist(MonitorPriceRow),
        },
    ]

    # Every model, grouped, each card linking straight to its changelist.
    context["model_groups"] = [
        {
            "title": "Ekranlar va hamkorlar",
            "cards": [
                {
                    "title": "Ekranlar",
                    "count": monitors_total,
                    "meta": f"{monitors_active} faol",
                    "icon": "tv",
                    "link": _changelist(Monitor),
                },
                {
                    "title": "Narx qatorlari",
                    "count": price_rows,
                    "meta": "Modal prays-list",
                    "icon": "sell",
                    "link": _changelist(MonitorPriceRow),
                },
                {
                    "title": "Hamkorlar",
                    "count": partners_total,
                    "meta": f"{partners_active} faol",
                    "icon": "handshake",
                    "link": _changelist(Partner),
                },
            ],
        },
        {
            "title": "Sayt kontenti",
            "cards": [
                {
                    "title": "Statistika",
                    "count": StatisticCard.objects.count(),
                    "meta": "About bo'limi",
                    "icon": "bar_chart",
                    "link": _changelist(StatisticCard),
                },
                {
                    "title": "Nega biz",
                    "count": WhyUsCard.objects.count(),
                    "meta": "Afzalliklar",
                    "icon": "star",
                    "link": _changelist(WhyUsCard),
                },
                {
                    "title": "Jarayon",
                    "count": ProcessCard.objects.count(),
                    "meta": "Qanday ishlaydi",
                    "icon": "format_list_numbered",
                    "link": _changelist(ProcessCard),
                },
                {
                    "title": "FAQ",
                    "count": faq_total,
                    "meta": f"{faq_active} faol",
                    "icon": "help",
                    "link": _changelist(FAQ),
                },
                {
                    "title": "Sozlamalar",
                    "count": SiteSettings.objects.count(),
                    "meta": "Aloqa va manzil",
                    "icon": "settings",
                    "link": _changelist(SiteSettings),
                },
            ],
        },
    ]

    return context
