from django.db import models
from django.db.models import CharField
from django.utils.text import slugify

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Region(TimeStampedModel):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    code = models.CharField(max_length=10, unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('sort_order', 'name')
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class District(TimeStampedModel):
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name='districts',
    )
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, blank=True)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('region__sort_order', 'sort_order', 'name')
        unique_together = (('region', 'name'), ('region', 'slug'))
        verbose_name = 'District'
        verbose_name_plural = 'Districts'

    def __str__(self):
        return f'{self.region.name} — {self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class TestModel(models.Model):
    title = models.IntegerField(default=0)
    count = models.CharField(max_length=120, null=True)


class Card(models.Model):
    title = models.CharField(max_length=120, default="0")
    count = models.IntegerField(null=True, default=0)


class Outdoor(models.Model):
    word = models.CharField(max_length=250, null=True)
    title = models.CharField(max_length=120, null=True)
    icon = models.ImageField(max_length=100, blank=True)
    steps = CharField(max_length=120, null=True)


from django.db import models


class StatisticCard(models.Model):
    title_ru = models.CharField(max_length=100)
    title_uz = models.CharField(max_length=100, blank=True, null=True)

    count = models.PositiveIntegerField()
    plus = models.BooleanField(default=False)

    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title_ru

    class Meta:
        ordering = ['order']




class WhyUsCard(models.Model):


    icon_image = models.ImageField(
        upload_to='why_us_icons/',
        blank=True,
        null=True,
        verbose_name="Icon rasm (ixtiyoriy)",
        help_text="Agar rasm sifatida icon yuklamoqchi bo'lsangiz, shu yerga yuklang"
    )
    icon_class = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Icon nomi (ixtiyoriy)",
        help_text="Masalan: 'map-pin', 'globe' — icon font ishlatilsa shu yerga yoziladi"
    )
    icon_svg = models.TextField(
        blank=True,
        verbose_name="Icon SVG kodi (ixtiyoriy)",
        help_text="To'liq <svg>...</svg> kodini shu yerga joylashtiring"
    )

    title = models.CharField(
        max_length=200,
        verbose_name="Sarlavha"
    )
    description = models.TextField(
        verbose_name="Tavsif"
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Tartib raqami",
        help_text="Kichik raqam birinchi chiqadi (0, 1, 2, 3...)"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Faol (saytda ko'rinadi)"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Karta (Nima uchun AHADMIX)"
        verbose_name_plural = "Kartalar (Nima uchun AHADMIX)"

    def __str__(self):
        return f"{self.order}. {self.title}"


from django.db import models


class ProcessCard(models.Model):
    number = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='icons/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return self.title





class Monitor(models.Model):
    title = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    address = models.TextField()

    image = models.ImageField(upload_to='led_screens/')

    screen_size = models.CharField(max_length=20)
    resolution = models.CharField(max_length=20)
    broadcast_time = models.CharField(max_length=50)

    contact_phone = models.CharField(max_length=20)
    contact_email = models.EmailField()
    video = models.FileField(upload_to='led_screens/videos/', blank=True, null=True)


    screen_format = models.CharField(
        max_length=50,
        default="Стандартный формат"
    )

    def __str__(self):
        return self.title


class PricePackage(models.Model):
    led_screen = models.ForeignKey(
        Monitor,
        on_delete=models.CASCADE,
        related_name='packages'
    )

    duration = models.PositiveIntegerField()
    views_per_month = models.PositiveIntegerField(default=9000)
    price = models.DecimalField(max_digits=12, decimal_places=0)  # so'm

    def __str__(self):
        return f"{self.duration} сек. - {self.price} сум"

# class Process(models.Model):
#     steps = CharField(max_length=120, null=True)

# models.py
