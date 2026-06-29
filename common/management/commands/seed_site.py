"""
Seed the database with all initial fixtures and download partner logos.

Usage:
    python manage.py seed_site                 # safe — skips if data already exists
    python manage.py seed_site --force         # wipes existing data first
    python manage.py seed_site --skip-logos    # don't download partner logos
"""

from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import transaction

from common.models import (
    SiteSettings, StatisticCard, WhyUsCard, ProcessCard,
    Monitor, MonitorPriceRow, Partner, FAQ,
)


class Command(BaseCommand):
    help = "Load fixtures and download partner logos in one go"

    def add_arguments(self, parser):
        parser.add_argument("--force", action="store_true",
                            help="Wipe existing data before loading")
        parser.add_argument("--skip-logos", action="store_true",
                            help="Don't download partner logos")

    def handle(self, *args, **options):
        force = options["force"]
        skip_logos = options["skip_logos"]

        existing = any([
            Monitor.objects.exists(),
            Partner.objects.exists(),
            FAQ.objects.exists(),
        ])
        if existing and not force:
            self.stdout.write(self.style.WARNING(
                "Data already exists. Use --force to wipe and reload."
            ))
            return

        if force:
            self.stdout.write("Wiping existing data…")
            with transaction.atomic():
                MonitorPriceRow.objects.all().delete()
                Monitor.objects.all().delete()
                Partner.objects.all().delete()
                FAQ.objects.all().delete()
                ProcessCard.objects.all().delete()
                WhyUsCard.objects.all().delete()
                StatisticCard.objects.all().delete()
                SiteSettings.objects.all().delete()

        self.stdout.write("Loading fixtures…")
        call_command("loaddata", "initial_data", verbosity=1)

        self.stdout.write(self.style.SUCCESS("Fixtures loaded."))

        if not skip_logos:
            self.stdout.write("\nDownloading partner logos…")
            call_command("download_partner_logos")

        self.stdout.write(self.style.SUCCESS("\nAll done. Site is ready."))