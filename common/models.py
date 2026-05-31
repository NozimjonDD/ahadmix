from django.db import models
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
