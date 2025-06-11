from django.db import models

from app.utils.rand import slugify_new


class Tags(models.Model):

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=255,
                            unique=True, default=None, blank=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f'{slugify_new(self.name)}'
        return super().save(*args, **kwargs)


class Category(models.Model):

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, default=None,
                            blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f'{slugify_new(self.name)}'
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'


class Page(models.Model):

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    title = models.CharField(max_length=65)
    slug = models.SlugField(max_length=255, default=None,
                            blank=True, unique=True)
    is_published = models.BooleanField(default=False)
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f'{slugify_new(self.title)}'
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'
