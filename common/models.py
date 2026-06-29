from django.db import models


class SiteSettings(models.Model):
    """Singleton — sayt sozlamalari"""
    phone = models.CharField(max_length=50, default="+998 94 657-33-33")
    email = models.EmailField(default="info@ahadmix.uz")

    address_ru = models.CharField(max_length=255, default="г. Ташкент, проспект Бунёдкора, 8а")
    address_uz = models.CharField(max_length=255, default="Toshkent sh., Bunyodkor shoh ko'chasi, 8a")
    address_en = models.CharField(max_length=255, default="Tashkent, Bunyodkor avenue 8a")

    telegram_link = models.URLField(default="https://linktr.ee/ahadmix_group")

    # Hero hisoblagichlari
    screens_count = models.PositiveIntegerField(default=70)
    years_on_market = models.PositiveIntegerField(default=16)
    brand_partners_count = models.PositiveIntegerField(default=500)

    kp_pdf = models.FileField(upload_to='docs/', blank=True, null=True,
                              help_text="Tijorat taklifi PDF (КП)")

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Site Settings"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class StatisticCard(models.Model):
    """Stats grid (about bo'limi)"""
    count = models.CharField(max_length=20)
    title_ru = models.CharField(max_length=255)
    title_uz = models.CharField(max_length=255, blank=True)
    title_en = models.CharField(max_length=255, blank=True)
    plus = models.BooleanField(default=False, help_text="Sonidan keyin '+' chiqsinmi")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.count} — {self.title_ru}"


class WhyUsCard(models.Model):
    """'Nega Ahadmix' bo'limi"""
    icon_svg = models.TextField(help_text="To'liq <svg>...</svg> kodi")

    title_ru = models.CharField(max_length=255)
    title_uz = models.CharField(max_length=255, blank=True)
    title_en = models.CharField(max_length=255, blank=True)

    description_ru = models.TextField()
    description_uz = models.TextField(blank=True)
    description_en = models.TextField(blank=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    @property
    def title(self):
        return self.title_ru

    @property
    def description(self):
        return self.description_ru

    def __str__(self):
        return self.title_ru


class ProcessCard(models.Model):
    """'Qanday ishlaydi' bo'limidagi qadamlar"""
    number = models.PositiveSmallIntegerField(unique=True)

    title_ru = models.CharField(max_length=255)
    title_uz = models.CharField(max_length=255, blank=True)
    title_en = models.CharField(max_length=255, blank=True)

    description_ru = models.TextField()
    description_uz = models.TextField(blank=True)
    description_en = models.TextField(blank=True)

    class Meta:
        ordering = ['number']

    @property
    def title(self):
        return self.title_ru

    @property
    def description(self):
        return self.description_ru

    def __str__(self):
        return f"{self.number:02d}. {self.title_ru}"


class Monitor(models.Model):
    """LED ekran — barcha ekranlar shu modeldan"""
    STATUS_CHOICES = [
        ('live', 'LIVE'),
        ('soon', 'СКОРО'),
    ]
    CATEGORY_CHOICES = [
        ('super', 'Super Format'),
        ('city', 'City'),
        ('district', 'District'),
    ]

    title = models.CharField(max_length=255, help_text="Ekran nomi (RU)")
    title_uz = models.CharField(max_length=255, blank=True)
    title_en = models.CharField(max_length=255, blank=True)

    location = models.TextField(help_text="To'liq manzil")
    location_uz = models.TextField(blank=True)
    location_en = models.TextField(blank=True)

    district = models.CharField(max_length=255, blank=True,
                                help_text="Tuman nomi (modalda chiqadi)")

    size = models.CharField(max_length=50, help_text="Masalan: 48×8 м")
    format = models.CharField(max_length=50, blank=True,
                              help_text="Tag (size bilan bir xil bo'lishi mumkin)")
    type_display = models.CharField(max_length=50, default='LED')
    resolution = models.CharField(max_length=50, blank=True)
    broadcast_hours = models.CharField(max_length=50, default='06:00–00:00')

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='city')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='live')

    image = models.ImageField(upload_to='monitors/', blank=True, null=True)
    video = models.FileField(upload_to='monitors/videos/', blank=True, null=True)

    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    is_featured = models.BooleanField(default=False,
                                      help_text="Asosiy 'Suparformat' gridda chiqadi")
    is_in_ticker = models.BooleanField(default=True,
                                       help_text="Yuqoridagi ticker chiziqda chiqadi")
    is_active = models.BooleanField(default=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


class MonitorPriceRow(models.Model):
    """Ekran prays-lis qatorlari (modalda chiqadi)"""
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE, related_name='price_rows')
    duration = models.CharField(max_length=50, help_text="Masalan: 10 сек")
    plays_per_month = models.CharField(max_length=50, help_text="Oyiga ko'rsatishlar soni")
    price = models.CharField(max_length=50, help_text="Faqat raqam, 'сум' template'da qo'shiladi")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.monitor.title} — {self.duration}"


class Partner(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='partners/')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class FAQ(models.Model):
    question_ru = models.CharField(max_length=500)
    question_uz = models.CharField(max_length=500, blank=True)
    question_en = models.CharField(max_length=500, blank=True)

    answer_ru = models.TextField()
    answer_uz = models.TextField(blank=True)
    answer_en = models.TextField(blank=True)

    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question_ru