from django.views.generic import TemplateView

from .models import (
    SiteSettings, StatisticCard, WhyUsCard, ProcessCard,
    Monitor, Partner, FAQ,
)


class IndexView(TemplateView):
    # Template: common/templates/common/index.html
    template_name = "common/index.html"

    # ---------- serializers ----------
    @staticmethod
    def _serialize_card(m):
        return {
            "n": m.title,
            "en": m.title_en or m.title,
            "uz": m.title_uz or m.title,
            "loc": m.location,
            "locEn": m.location_en or m.location,
            "locUz": m.location_uz or m.location,
            "tag": m.size,
            "tagEn": m.size,
            "video": m.video.url if m.video else "",
            "photo": m.image.url if m.image else "",
            "soon": m.status == "soon",
        }

    @staticmethod
    def _serialize_details(m):
        media = ""
        if m.video:
            media = m.video.url
        elif m.image:
            media = m.image.url

        return {
            "n": m.title,
            "a": m.location,
            "d": m.district or "—",
            "sz": m.size,
            "f": m.format or m.size,
            "res": m.resolution or "—",
            "hrs": m.broadcast_hours or "—",
            "media": media,
            "soon": m.status == "soon",
            "live": m.status == "live",
            "rows": [
                [r.duration, r.plays_per_month, r.price]
                for r in m.price_rows.all()
            ],
        }

    # ---------- context ----------
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        # Settings (singleton)
        settings_obj = SiteSettings.load()
        ctx["settings"] = settings_obj

        # Section content
        ctx["statisticcard"] = StatisticCard.objects.all()
        ctx["why_us_cards"] = WhyUsCard.objects.all()
        ctx["processcard"] = ProcessCard.objects.all()

        # Monitors
        all_monitors = (
            Monitor.objects
            .filter(is_active=True)
            .prefetch_related("price_rows")
        )
        featured = all_monitors.filter(is_featured=True)
        ticker = all_monitors.filter(is_in_ticker=True)
        on_map = all_monitors.exclude(latitude__isnull=True).exclude(longitude__isnull=True)

        ctx["featured_monitors"] = featured
        ctx["all_monitors"] = all_monitors

        # Backwards-compat with older template references
        ctx["card"] = {"monitors": featured, "monitor": all_monitors}

        # Partners & FAQs
        partners = Partner.objects.filter(is_active=True)
        faqs = FAQ.objects.filter(is_active=True)
        ctx["partners"] = partners
        ctx["faqs"] = faqs

        # ---------- JSON payloads for JS ----------
        ctx["ticker_names_json"] = list(ticker.values_list("title", flat=True))

        ctx["featured_monitors_json"] = [self._serialize_card(m) for m in featured]

        ctx["partners_json"] = [
            {"n": p.name, "u": p.logo.url if p.logo else ""}
            for p in partners
        ]

        ctx["faqs_json"] = [
            {
                "q": f.question_ru,
                "qUz": f.question_uz or f.question_ru,
                "qEn": f.question_en or f.question_ru,
                "a": f.answer_ru,
                "aUz": f.answer_uz or f.answer_ru,
                "aEn": f.answer_en or f.answer_ru,
            }
            for f in faqs
        ]

        ctx["map_points_json"] = [
            [m.latitude, m.longitude, m.title, m.size]
            for m in on_map
        ]

        ctx["all_monitors_json"] = [
            [
                m.title,
                m.size,
                m.location,
                (m.video.url if m.video else (m.image.url if m.image else "")),
            ]
            for m in all_monitors
        ]

        ctx["screen_details_json"] = [
            self._serialize_details(m) for m in all_monitors
        ]

        return ctx