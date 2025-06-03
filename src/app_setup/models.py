from django.db import models


class MenuLink(models.Model):
    class Meta:
        verbose_name = "Menu link"
        verbose_name_plural = "Menu links"
    text = models.CharField(max_length=50)
    url_or_path = models.CharField(max_length=2048)
    new_tab = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.text}'
