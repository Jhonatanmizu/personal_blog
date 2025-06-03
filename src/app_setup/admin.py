from django.contrib import admin

from .models import MenuLink


@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = 'text', 'url_or_path', 'id'
    list_display_links = 'text', 'url_or_path', 'id'
    search_fields = "id", "text", "url_or_path"
