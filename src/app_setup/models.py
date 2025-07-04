
from django.db import models

from app.utils import images, model_validators


class MenuLink(models.Model):
    class Meta:
        verbose_name = "Menu link"
        verbose_name_plural = "Menu links"
    text = models.CharField(max_length=50)
    url_or_path = models.CharField(max_length=2048)
    new_tab = models.BooleanField(default=False)
    site_setup = models.ForeignKey(
        'SiteSetup', on_delete=models.CASCADE, null=True, blank=True, default=None
    )
    objects = models.Manager()

    def __str__(self) -> str:
        return f'{self.text}'


class SiteSetup(models.Model):
    class Meta:
        verbose_name = 'Setup'
        verbose_name_plural = 'Setup'

    title = models.CharField(max_length=65)
    description = models.CharField(max_length=255)
    show_header = models.BooleanField(default=True)
    show_search = models.BooleanField(default=True)
    show_menu = models.BooleanField(default=True)
    show_description = models.BooleanField(default=True)
    show_pagination = models.BooleanField(default=True)
    show_footer = models.BooleanField(default=True)
    favicon = models.ImageField(
        upload_to='assets/favicon/%Y/%m/', blank=True, default='', validators=(model_validators.validate_img_png,))
    objects = models.Manager()

    def save(self, *args, **kwargs) -> None:
        current_favicon_name = str(self.favicon.name)
        super().save(*args, **kwargs)
        favicon_changed = False
        if self.favicon:
            favicon_changed = current_favicon_name != self.favicon.name

        if favicon_changed:
            images.resize_image(self.favicon, 32)

    def __str__(self):
        return f'{self.title}'
