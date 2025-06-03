from django.contrib import admin
from django.http import HttpRequest

from .models import MenuLink, SiteSetup


@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = 'text', 'url_or_path', 'id'
    list_display_links = 'text', 'url_or_path', 'id'
    search_fields = "id", "text", "url_or_path"


@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = 'title', 'description',

    def has_add_permission(self, request: HttpRequest) -> bool:
        return not SiteSetup.objects.exists()
