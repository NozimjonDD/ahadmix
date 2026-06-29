"""
Download partner logos from ahadmix.com into local media/partners/ folder.

Usage:
    python manage.py download_partner_logos
"""

import os
import urllib.request
from urllib.error import URLError, HTTPError

from django.conf import settings
from django.core.management.base import BaseCommand

from common.models import Partner


PARTNER_BASE = "https://ahadmix.com/media/"


class Command(BaseCommand):
    help = "Download partner logos from ahadmix.com into MEDIA_ROOT/partners/"

    def add_arguments(self, parser):
        parser.add_argument(
            "--force",
            action="store_true",
            help="Re-download even if file already exists",
        )

    def handle(self, *args, **options):
        force = options["force"]
        partners_dir = os.path.join(settings.MEDIA_ROOT, "partners")
        os.makedirs(partners_dir, exist_ok=True)

        partners = Partner.objects.all()
        total = partners.count()
        if total == 0:
            self.stdout.write(self.style.WARNING(
                "No partners in database. Load fixtures first:\n"
                "  python manage.py loaddata initial_data"
            ))
            return

        ok, skipped, failed = 0, 0, 0
        for p in partners:
            if not p.logo:
                self.stdout.write(self.style.WARNING(f"  – {p.name}: no logo path set"))
                failed += 1
                continue

            rel_path = str(p.logo)  # e.g. partners/1724749722645-SAMSUNGverq.png
            local_path = os.path.join(settings.MEDIA_ROOT, rel_path)
            filename = os.path.basename(rel_path)
            url = PARTNER_BASE + filename

            if os.path.exists(local_path) and not force:
                self.stdout.write(f"  ✓ {p.name}: already exists")
                skipped += 1
                continue

            try:
                req = urllib.request.Request(
                    url,
                    headers={"User-Agent": "Mozilla/5.0 (download_partner_logos)"},
                )
                with urllib.request.urlopen(req, timeout=20) as resp, \
                        open(local_path, "wb") as out:
                    out.write(resp.read())
                self.stdout.write(self.style.SUCCESS(f"  ↓ {p.name}: {filename}"))
                ok += 1
            except (URLError, HTTPError, OSError) as e:
                self.stdout.write(self.style.ERROR(f"  ✗ {p.name}: {e}"))
                failed += 1

        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS(
            f"Done. Downloaded: {ok}, skipped: {skipped}, failed: {failed} "
            f"(total: {total})"
        ))